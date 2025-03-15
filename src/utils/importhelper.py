import json
import os
from typing import Any, Dict, Optional

class ImportHelper:
    @staticmethod
    def load_json_file(file_path: str) -> Dict[str, Any]:
        """
        Load and parse a JSON file.
        
        Args:
            file_path (str): Path to the JSON file
            
        Returns:
            Dict[str, Any]: Parsed JSON content
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def load_text_file(file_path: str) -> str:
        """
        Load a text file.
        
        Args:
            file_path (str): Path to the text file
            
        Returns:
            str: Content of the text file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def get_file_path(relative_path: str, base_dir: Optional[str] = None) -> str:
        """
        Get absolute file path from relative path.
        
        Args:
            relative_path (str): Relative path to the file
            base_dir (Optional[str]): Base directory to resolve relative path from
            
        Returns:
            str: Absolute path to the file
        """
        if base_dir is None:
            base_dir = os.getcwd()
        return os.path.abspath(os.path.join(base_dir, relative_path)) 