# pylint: disable=C0301,W0212,R0902,R0903,R0801
"""Class to handle all calls with s3"""

import json
import boto3

class S3Manager:
    """s3 manager"""

    s3_client = None
    logger = None

    def __init__(self, logger, s3_client=None):
        """Allows you to pass Boto3 Client in """
        self.logger = logger
        if s3_client is not None:
            self.s3_client = s3_client
        else:
            self.s3_client = boto3.client('s3')
            self.logger.info('New boto3 (S3 client) instantiated')


    def send_message_body_to_s3(self, bucket, key, body):
        """Function to Send messages to s3"""
        self.logger.info("bucket = {bucket}, key = {key}".format(bucket=bucket, key=key))
        self.s3_client.put_object(Body=json.dumps(body), Bucket=bucket, Key=key)
        return True

    def put_object(self, bucket, key, body):
        """puts object contents in s3"""
        self.logger.info("bucket = {bucket}, key = {key}, body = {body}".format(bucket=bucket, key=key, body=body))
        self.s3_client.put_object(Bucket=bucket, Key=key, Body=body)
        return True
