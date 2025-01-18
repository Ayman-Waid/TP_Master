import unittest
from unittest.mock import patch, mock_open
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)
def log_error(msg):
    logging.error(msg)

def read_file(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        log_error(f"File not found: {fileName}")
        print("File not found")
    finally:
        print("File processing completed.")

class TestReadFile(unittest.TestCase):

    @patch("builtins.open", side_effect=FileNotFoundError)
    @patch("logging.error")
    def test_file_not_found(self, mock_logging_error, mock_open):
        read_file("non_existent_file.txt")
        mock_logging_error.assert_called_once_with("File not found: non_existent_file.txt")

    @patch("builtins.open", new_callable=mock_open, read_data="This is a test file.")
    def test_file_read_success(self, mock_open):
        with patch("builtins.print") as mock_print:
            read_file("existent_file.txt")
            mock_print.assert_any_call("This is a test file.")
            mock_print.assert_any_call("File processing completed.")

    @patch("builtins.open", side_effect=PermissionError)
    @patch("logging.error")
    def test_permission_error(self, mock_logging_error, mock_open):
        read_file("protected_file.txt")
        mock_logging_error.assert_not_called()

if __name__ == "__main__":
    unittest.main()
