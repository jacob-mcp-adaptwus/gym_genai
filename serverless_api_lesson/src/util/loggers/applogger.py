# We're going to use attributes instead of docstrings
# pylint: disable=C0111

import logging
import logging.config
import copy
import json
import time

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'streaming': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['streaming'],
            'level': 'INFO',
        },
    }
}

logging.config.dictConfig(LOGGING)


class AppLogger:

    metadata = None
    loggername = None
    start = None

    def __init__(self, loggername):

        self.start = time.time()
        self.metadata = dict()
        self.loggername = loggername
        self.logger = logging.getLogger(loggername)


    def debug(self, msg, *args, **kwargs):
        msg = self.format_metadata() + msg
        self.logger.debug(msg, *args, **kwargs)


    def info(self, msg, *args, **kwargs):
        msg = self.format_metadata() + msg
        self.logger.info(msg, *args, **kwargs)


    def warning(self, msg, *args, **kwargs):
        msg = self.format_metadata() + msg
        self.logger.warning(msg, *args, **kwargs)


    def error(self, msg, *args, **kwargs):
        msg = self.format_metadata() + msg
        self.logger.error(msg, *args, **kwargs)


    def fatal(self, msg, *args, **kwargs):
        msg = self.format_metadata() + msg
        self.logger.fatal(msg, *args, **kwargs)


    def exception(self, msg, *args, exc_info=True, **kwargs):
        msg = self.format_metadata() + msg
        self.logger.exception(msg, *args, exc_info=exc_info, **kwargs)


    def for_splunk(self, msg, payload, addtional_dict=None):
        if not isinstance(payload, (dict)):
            raise Exception('payload is not dict it is of ' + str(type(payload)))
        copy_payload = copy.deepcopy(payload)
        copy_payload['msg'] = msg
        copy_payload['logger'] = self.loggername
        if addtional_dict is not None:
            if not isinstance(addtional_dict, (dict)):
                raise Exception('addtional_dict needs to be of type dict')
            for key in addtional_dict:
                copy_payload[key] = addtional_dict[key]
        for key in self.metadata:
            copy_payload[key] = self.metadata[key]
        copy_payload['Authorization'] = 'xxxx'
        print(json.dumps(copy_payload))

    def set_metadata(self, key_values):
        if key_values is not None:
            self.metadata = key_values
        else:
            # We always want an object even if
            # it doesn't have anything in it because
            # we aren't checking for null when we
            # iterate over it.
            self.metadata = dict()


    @staticmethod
    def noisy_libs():
        return ['boto3', 'botocore']

    def format_metadata(self):
        end = time.time()
        self.metadata['timer'] = str(end - self.start)
        text = ""
        for key, val in self.metadata.items():
            text += "{}={},  ".format(key, val)

        return text

    # disable this warning because we need to
    # override a runtime method name
    # pylint: disable=C0103
    def setLevel(self, level: str):

        # Normalize the value
        log_level = level.upper()

        if log_level == "DEBUG":
            self.logger.info("Setting log level to %s", log_level)
            self.logger.setLevel(logging.DEBUG)

            # This will quiet the noisy libraries by changing their
            # log level to something strict
            for lib in self.noisy_libs():
                logging.getLogger(lib).setLevel(logging.CRITICAL)

        elif log_level == "INFO":
            self.logger.info("Setting log level to %s", log_level)
            self.logger.setLevel(logging.INFO)
        elif log_level == "WARNING":
            self.logger.info("Setting log level to %s", log_level)
            self.logger.setLevel(logging.WARNING)
        elif log_level == "ERROR":
            self.logger.info("Setting log level to %s", log_level)
            self.logger.setLevel(logging.ERROR)
        elif log_level == "CRITICAL":
            self.logger.info("Setting log level to %s", log_level)
            self.logger.setLevel(logging.CRITICAL)
        else:
            # Unknown or unset value, so set a default of
            # warning so we don't by default generate spam.
            # Said differently, make someone have to take an
            # action to get the more verbose levels
            self.logger.setLevel(logging.WARNING)
            if not log_level:
                self.logger.warning(
                    "The LOG_LEVEL environment variable is not set. Please set it to "
                    "a valid value of DEBUG, INFO, WARNING, ERROR, or CRITICAL. ")
            else:
                self.logger.warning(
                    "The LOG_LEVEL environment variable value specified (\"%s\") "
                    "is unknown. Valid values are DEBUG, INFO, WARNING, ERROR, or CRITICAL. "
                    "Setting default level to WARNING", log_level)

            self.logger.warning("Using the default log level setting of WARNING")

        self.logger.setLevel(log_level)
