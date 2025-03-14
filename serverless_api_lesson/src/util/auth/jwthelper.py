# Class to help format lambda requests
# pylint: disable=C0111
from datetime import datetime, timedelta
import jwt

class JwtHelper:
    """jwt helper class"""
    logger = None
    token = None
    object_dict = None
    secret = None
    algorithm = "HS256"
    bearer_str = 'Bearer '

    def __init__(self, secret):
        """Init"""
        self.secret = secret

    def get_token_from_header(self, bearer):
        """removing extra text in bearer token"""
        bearer = bearer.replace(self.bearer_str, '')
        return bearer

    def encode(self, object_dict):
        """encodes dict into token"""
        object_dict["exp"] = datetime.now() + timedelta(days=2)
        encoded_jwt = jwt.encode(object_dict, self.secret, algorithm=self.algorithm)
        return encoded_jwt

    def decode(self, token):
        """decodes token into dict"""
        token = self.get_token_from_header(token)
        decoded = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        return decoded
