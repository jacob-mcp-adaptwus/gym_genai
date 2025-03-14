# pylint: disable=C0111,R0201
# We're going to use attributes instead of docstrings
import json


class ImportHelper:
    ref = None

    @staticmethod
    def get_json(file_path):
        data = ImportHelper.get_file(file_path)
        return json.loads(data)


    @staticmethod
    def get_file(file_path):
        """gets files"""
        try:
            with open(file_path) as file:
                return return_file(file)
        except FileNotFoundError:
            ## for testing
            with open('src/' + file_path) as file:
                return return_file(file)


def return_file(file):
    """returns File"""
    data = file.read()
    file.close()
    return data
