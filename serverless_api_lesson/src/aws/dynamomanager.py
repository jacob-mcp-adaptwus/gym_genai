# pylint: disable=C0301,W0212,R0902,R0903,R0801
"""Class to handle all calls with s3"""
from decimal import Decimal
import time
import boto3
from boto3.dynamodb.conditions import Key

class DynamoManager:
    """s3 manager"""

    dynamo_client = None
    logger = None

    def __init__(self, logger):
        """Allows you to pass Boto3 Client in """
        self.logger = logger
        self.dynamo_client = boto3.resource('dynamodb', region_name='us-east-1')

    def upsert(self, table_name, filter_key, filter_value, object_to_write):
        """dynamo upsert"""
        user_obj = self.get_dynamo_item(table_name, filter_key, filter_value)
        for key in object_to_write:
            user_obj[key] = object_to_write[key]
        self.put_dynamo_item(table_name, user_obj)
        return True

    def delete_item(self, key_dict, table_name):
        """delete item function key should be of type dict"""
        table = self.dynamo_client.Table(table_name)
        resp = table.delete_item(Key=key_dict)
        print(resp)
        return True

    def put_dynamo_item(self, table_name, payload):
        """puts items into dynamodb"""
        table = self.dynamo_client.Table(table_name)
        table.put_item(
            Item=payload
        )
        return True

    def get_dynamo_item(self, table_name, filter_key, filter_value):
        """gets items from dynamodb"""
        table = self.dynamo_client.Table(table_name)
        response = table.get_item(Key={filter_key:filter_value})
        item = response['Item']
        return item

    def get_dynamo_item_multi_key(self, table_name, lookup_keys):
        """get itmes with mutliple keys"""
        table = self.dynamo_client.Table(table_name)
        response = table.get_item(Key=lookup_keys)
        item = response['Item']
        return item

    def put_if_not_exisits_multi_key(self, table_name, lookup_keys, object_to_write):
        """puts item in dynamo if not exisits"""
        try:
            return self.get_dynamo_item_multi_key(table_name, lookup_keys)
        except KeyError:
            self.logger.info('no items found, inserting')
            self.put_dynamo_item(table_name, object_to_write)
            return object_to_write

    def put_if_not_exisits(self, table_name, filter_key, filter_value, object_to_write):
        """puts item in dynamo if not exisits"""
        try:
            return self.get_dynamo_item(table_name, filter_key, filter_value)
        except KeyError:
            self.logger.info('no items found, inserting')
            self.put_dynamo_item(table_name, object_to_write)
            return object_to_write

    def scan_table(self, table_name, filter_key=None, filter_value=None):
        """Perform a scan operation on table. Can specify filter_key (col name) and its value to be filtered."""
        start = time.time()
        table = self.dynamo_client.Table(table_name)
        if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = table.scan(FilterExpression=filtering_exp)
            data = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'], FilterExpression=filtering_exp)
                data.extend(response['Items'])
        else:
            response = table.scan()
            data = response['Items']
        end = time.time()
        self.logger.info('Scan Table Time: ' + str(end - start))
        return data

    def query_table(self, table_name, filter_key, filter_value):
        """Perform a query operation on table with Decimal conversion"""
        start = time.time()
        table = self.dynamo_client.Table(table_name)
        message = f"query on {table_name} for the column {filter_key} for {filter_value}"
        self.logger.info(message)
        
        response = table.query(
            KeyConditionExpression=Key(filter_key).eq(filter_value)
        )
        
        data = [self._convert_item(item) for item in response['Items']]
        
        end = time.time()
        self.logger.info(f'Query Table Time: {str(end - start)}  {str(data)}')
        return data

    def _convert_item(self, item):
        """Convert Decimal values in an item to float"""
        if isinstance(item, dict):
            return {key: float(value) if isinstance(value, Decimal) else value 
                   for key, value in item.items()}
        return item