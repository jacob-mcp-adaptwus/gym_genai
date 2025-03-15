# pylint: disable=R0903
"""secrets managing"""
import json
import boto3
from botocore.exceptions import ClientError


class SecretManager:
    """Class for managing Secrets"""
    service_name = 'secretsmanager'

    def get(self, secret_name):
        """gets Secrets"""

        # Create a Secrets Manager client
        session = boto3.session.Session()
        region_name = session.region_name
        client = session.client(
            service_name=self.service_name,
            region_name=region_name
        )

        # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValuerror_e.html
        # We rethrow the exception by default.
        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as error_e:
            raise error_e

        if 'SecretString' in get_secret_value_response:
            get_secret_value_response = get_secret_value_response['SecretString']


        if get_secret_value_response is None:
            raise NameError(
                "Expected to find a secret named {} in the AWS Secret Manager. "
                "However, none was found. Please check the AWS Secret Manager "
                "to make sure the secret exist under the specified name.".format(secret_name)
            )

        if isinstance(get_secret_value_response, str):
            get_secret_value_response = json.loads(get_secret_value_response)

        return get_secret_value_response
