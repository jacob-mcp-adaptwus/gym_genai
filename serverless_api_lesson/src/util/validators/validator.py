# pylint: disable=R0903, C0301, W0703, R0201
"""for validating payloads"""
from jsonschema import validate


class Validator:
    """Class for parsing payloads"""
    error_msg = None
    def __init__(self, logger):
        """ init"""
        self.logger = logger

    def validate_payload(self, payload, schema):
        """validate schema"""
        if not isinstance(payload, (dict)) or not isinstance(schema, (dict)):
            raise TypeError('Both arguments should be of type dict')
        valid_payload = None
        try:
            validate(instance=payload, schema=schema)
            valid_payload = True
        except Exception as error_e:
            valid_payload = False
            cleaned = str(error_e)
            cleaned = cleaned.replace('\n', ' ')
            self.logger.info(str(cleaned))
            split = str(error_e).split('\n')
            self.error_msg = split[0]  + self.find_where_in_instance(split)
        return valid_payload

    def find_where_in_instance(self, array):
        """function to find where in the payload the validation failed"""
        for element in array:
            if 'On instance' in element:
                if abs(len(element) - len('On instance')) <= 2:
                    return ''
                return ', ' + element
        return ''
