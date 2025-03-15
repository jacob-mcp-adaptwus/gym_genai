import logging
import json
from typing import Any, Dict, Optional

class AppLogger:
    def __init__(self, name: str = "AppLogger"):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def _format_message(self, message: Any, additional_info: Optional[Dict] = None) -> str:
        if isinstance(message, (dict, list)):
            message = json.dumps(message)
        if additional_info:
            return f"{message} | Additional Info: {json.dumps(additional_info)}"
        return str(message)

    def info(self, message: Any, additional_info: Optional[Dict] = None) -> None:
        self.logger.info(self._format_message(message, additional_info))

    def error(self, message: Any, additional_info: Optional[Dict] = None) -> None:
        self.logger.error(self._format_message(message, additional_info))

    def warning(self, message: Any, additional_info: Optional[Dict] = None) -> None:
        self.logger.warning(self._format_message(message, additional_info))

    def debug(self, message: Any, additional_info: Optional[Dict] = None) -> None:
        self.logger.debug(self._format_message(message, additional_info))

    def critical(self, message: Any, additional_info: Optional[Dict] = None) -> None:
        self.logger.critical(self._format_message(message, additional_info)) 