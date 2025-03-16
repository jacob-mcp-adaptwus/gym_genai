"""Class to handle all S3 operations for the bodybuilding app"""
import json
from typing import Dict, Any, Optional, BinaryIO
import boto3
from botocore.exceptions import ClientError

class S3Manager:
    """S3 manager for handling file operations in the bodybuilding app"""

    def __init__(self, logger, s3_client=None):
        """Initialize S3 manager with logger and optional client"""
        self.logger = logger
        self.s3_client = s3_client or boto3.client('s3')
        self.logger.info('S3 manager initialized')

    def upload_json(self, bucket: str, key: str, data: Dict[str, Any]) -> bool:
        """Upload JSON data to S3"""
        try:
            self.logger.info(f"Uploading JSON to s3://{bucket}/{key}")
            self.s3_client.put_object(
                Body=json.dumps(data, indent=2),
                Bucket=bucket,
                Key=key,
                ContentType='application/json'
            )
            return True
        except ClientError as e:
            self.logger.error(f"Failed to upload JSON to S3: {str(e)}")
            raise

    def download_json(self, bucket: str, key: str) -> Dict[str, Any]:
        """Download and parse JSON data from S3"""
        try:
            self.logger.info(f"Downloading JSON from s3://{bucket}/{key}")
            response = self.s3_client.get_object(Bucket=bucket, Key=key)
            return json.loads(response['Body'].read().decode('utf-8'))
        except ClientError as e:
            self.logger.error(f"Failed to download JSON from S3: {str(e)}")
            raise

    def upload_file(self, bucket: str, key: str, file_obj: BinaryIO, content_type: Optional[str] = None) -> bool:
        """Upload a file object to S3"""
        try:
            self.logger.info(f"Uploading file to s3://{bucket}/{key}")
            extra_args = {'ContentType': content_type} if content_type else {}
            self.s3_client.upload_fileobj(file_obj, bucket, key, ExtraArgs=extra_args)
            return True
        except ClientError as e:
            self.logger.error(f"Failed to upload file to S3: {str(e)}")
            raise

    def download_file(self, bucket: str, key: str, file_path: str) -> bool:
        """Download a file from S3 to local filesystem"""
        try:
            self.logger.info(f"Downloading s3://{bucket}/{key} to {file_path}")
            self.s3_client.download_file(bucket, key, file_path)
            return True
        except ClientError as e:
            self.logger.error(f"Failed to download file from S3: {str(e)}")
            raise

    def delete_object(self, bucket: str, key: str) -> bool:
        """Delete an object from S3"""
        try:
            self.logger.info(f"Deleting s3://{bucket}/{key}")
            self.s3_client.delete_object(Bucket=bucket, Key=key)
            return True
        except ClientError as e:
            self.logger.error(f"Failed to delete object from S3: {str(e)}")
            raise

    def list_objects(self, bucket: str, prefix: str = '') -> list:
        """List objects in an S3 bucket with optional prefix"""
        try:
            self.logger.info(f"Listing objects in s3://{bucket}/{prefix}")
            paginator = self.s3_client.get_paginator('list_objects_v2')
            objects = []
            
            for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
                if 'Contents' in page:
                    objects.extend(page['Contents'])
                    
            return objects
        except ClientError as e:
            self.logger.error(f"Failed to list objects in S3: {str(e)}")
            raise

    def object_exists(self, bucket: str, key: str) -> bool:
        """Check if an object exists in S3"""
        try:
            self.s3_client.head_object(Bucket=bucket, Key=key)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                return False
            self.logger.error(f"Error checking object existence in S3: {str(e)}")
            raise

    def get_object_metadata(self, bucket: str, key: str) -> Dict[str, Any]:
        """Get metadata for an S3 object"""
        try:
            response = self.s3_client.head_object(Bucket=bucket, Key=key)
            return {
                'size': response['ContentLength'],
                'last_modified': response['LastModified'],
                'content_type': response.get('ContentType'),
                'metadata': response.get('Metadata', {}),
                'e_tag': response.get('ETag'),
            }
        except ClientError as e:
            self.logger.error(f"Failed to get object metadata from S3: {str(e)}")
            raise 