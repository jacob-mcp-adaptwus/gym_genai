#Class to help format lambda requests
#pylint: disable=C0111,C0301,E1101,R0903
#import ldap
import requests

class LdapAuth:

    logger = None

    def __init__(self, logger):
        """Init"""
        self.logger = logger

    def authorize_ldap(self, username, password):
        ##
        url = "https://sta6bdxquf.execute-api.us-west-1.amazonaws.com/dev/login"
        payload = {
            "username": username,
            "password": password
            }
        response = requests.request("POST", url, json=payload)
        self.logger.info(response.text)
        if response.status_code not in [200, 201, 202, 203, 204]:
            return False
        return True
