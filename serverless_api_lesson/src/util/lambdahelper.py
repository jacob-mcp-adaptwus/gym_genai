# Class to help format lambda requests
# pylint: disable=C0111,C0301
import json


class LambdaHelper:

    headers = {
        'access-control-allow-origin':'*',
        'access-control-allow-methods': 'DELETE,POST,GET,OPTIONS,PUT',
        'access-control-allow-credentials': True,
        'access-control-max-age': 900,
        'access-control-allow-headers': """x-token,x-tto-engine-version,date,intuit_originatingip,content-length,expires,vary,origin,authorization,keep-alive,content-disposition,content-transfer-encoding,if-unmodified-since,content-md5,fragment-location,content-type,connection,if-match,cache-control,intuit_tid,x-tto-routing-info,pragma,intuit_orignalurl,accept,x-requested-with,content-location,content-range,etag,intuit_originalurl"""
        }
    logger = None

    def __init__(self, logger):
        """Init"""
        self.logger = logger

    def format_response(self, status_code, body, headers=None):
        """static function to format response"""
        if not isinstance(status_code, (int)):
            raise TypeError('Status Code needs to be of type integer')
        if headers is None:
            payload = {
                "statusCode": status_code,
                "body": json.dumps(body),
                "headers": self.headers
                }
            self.logger.info("response payload: %s ", json.dumps(payload))
            return payload
        payload = {
            "statusCode": status_code,
            "body": json.dumps(body),
            "headers": headers
            }
        self.logger.info("response payload: %s ", json.dumps(payload))
        return payload

    def set_headers(self, header):
        self.headers = header
