"""Class to handle all DynamoDB operations for the bodybuilding app"""
from decimal import Decimal
import time
import boto3
from boto3.dynamodb.conditions import Key

class DynamoManager:
    """DynamoDB manager for bodybuilding app"""

    def __init__(self, logger):
        """Initialize DynamoDB client"""
        self.logger = logger
        self.dynamo_client = boto3.resource('dynamodb', region_name='us-east-1')

    def upsert(self, table_name, filter_key, filter_value, object_to_write):
        """Update or insert an item in DynamoDB"""
        try:
            existing_obj = self.get_dynamo_item(table_name, filter_key, filter_value)
            for key in object_to_write:
                existing_obj[key] = object_to_write[key]
            self.put_dynamo_item(table_name, existing_obj)
        except KeyError:
            self.put_dynamo_item(table_name, object_to_write)
        return True

    def delete_item(self, key_dict, table_name):
        """Delete an item from DynamoDB"""
        table = self.dynamo_client.Table(table_name)
        response = table.delete_item(Key=key_dict)
        self.logger.info(f"Deleted item from {table_name}: {response}")
        return True

    def put_dynamo_item(self, table_name, payload):
        """Put an item into DynamoDB"""
        table = self.dynamo_client.Table(table_name)
        table.put_item(Item=payload)
        return True

    def get_dynamo_item(self, table_name, filter_key, filter_value):
        """Get a single item from DynamoDB"""
        table = self.dynamo_client.Table(table_name)
        response = table.get_item(Key={filter_key: filter_value})
        return response['Item']

    def get_dynamo_item_multi_key(self, table_name, lookup_keys):
        """Get an item using multiple keys"""
        table = self.dynamo_client.Table(table_name)
        response = table.get_item(Key=lookup_keys)
        return response['Item']

    def put_if_not_exists_multi_key(self, table_name, lookup_keys, object_to_write):
        """Put an item only if it doesn't exist (using multiple keys)"""
        try:
            return self.get_dynamo_item_multi_key(table_name, lookup_keys)
        except KeyError:
            self.logger.info(f'No item found in {table_name}, inserting new item')
            self.put_dynamo_item(table_name, object_to_write)
            return object_to_write

    def put_if_not_exists(self, table_name, filter_key, filter_value, object_to_write):
        """Put an item only if it doesn't exist"""
        try:
            return self.get_dynamo_item(table_name, filter_key, filter_value)
        except KeyError:
            self.logger.info(f'No item found in {table_name}, inserting new item')
            self.put_dynamo_item(table_name, object_to_write)
            return object_to_write

    def scan_table(self, table_name, filter_key=None, filter_value=None):
        """Scan a DynamoDB table with optional filtering"""
        start_time = time.time()
        table = self.dynamo_client.Table(table_name)
        
        if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = table.scan(FilterExpression=filtering_exp)
            data = response['Items']
            
            while 'LastEvaluatedKey' in response:
                response = table.scan(
                    ExclusiveStartKey=response['LastEvaluatedKey'],
                    FilterExpression=filtering_exp
                )
                data.extend(response['Items'])
        else:
            response = table.scan()
            data = response['Items']
            
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                data.extend(response['Items'])

        end_time = time.time()
        self.logger.info(f'Scan table {table_name} completed in {end_time - start_time} seconds')
        return [self._convert_item(item) for item in data]

    def query_table(self, table_name, filter_key, filter_value):
        """Query a DynamoDB table"""
        start_time = time.time()
        table = self.dynamo_client.Table(table_name)
        
        self.logger.info(f"Querying {table_name} where {filter_key} = {filter_value}")
        response = table.query(
            KeyConditionExpression=Key(filter_key).eq(filter_value)
        )
        
        data = [self._convert_item(item) for item in response['Items']]
        
        while 'LastEvaluatedKey' in response:
            response = table.query(
                KeyConditionExpression=Key(filter_key).eq(filter_value),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            data.extend([self._convert_item(item) for item in response['Items']])

        end_time = time.time()
        self.logger.info(f'Query completed in {end_time - start_time} seconds')
        return data

    def _convert_item(self, item):
        """Convert DynamoDB Decimal types to float"""
        if isinstance(item, dict):
            return {
                key: (float(value) if isinstance(value, Decimal) else 
                     self._convert_item(value) if isinstance(value, (dict, list)) else value)
                for key, value in item.items()
            }
        elif isinstance(item, list):
            return [self._convert_item(value) for value in item]
        return item 