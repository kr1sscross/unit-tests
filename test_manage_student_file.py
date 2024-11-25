import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import os

class TestManageStudentFile(unittest.TestCase):

    @patch('builtins.input', side_effect=["yes", "John", "Doe", "12345"])
    @patch('os.path.isfile', return_value=False)
    @patch('builtins.open', new_callable=mock_open)
    def test_create_new_file(self, mock_open, mock_isfile, mock_input):
        from mfile import manage_student_file
        manage_student_file()
        mock_open.assert_called_with("list.txt", mode='a')
        mock_open().write.assert_any_call("First Name,Last Name,ID\n")
        mock_open().write.assert_any_call("John,Doe,12345\n")

    @patch('builtins.input', side_effect=["no"])
    @patch('os.path.isfile', return_value=True)
    def test_no_addition(self, mock_isfile, mock_input):
        from plik1 import manage_student_file
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manage_student_file()
            self.assertIn("Operation terminated.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
