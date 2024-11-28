import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import os
from main import manage_student_file

# Kod nie działa, do poprawy

class TestManageStudentFile(unittest.TestCase):

    @patch('builtins.input', side_effect=["yes", "John", "Doe", "125"])
    @patch('os.path.isfile', return_value=False)
    @patch('builtins.open', new_callable=mock_open)
    def test_create_new_file(self, mock_open, mock_isfile, mock_input):
        manage_student_file()
        mock_open.assert_called_with("list.txt", mode='a')
        mock_open().write.assert_any_call("First Name,Last Name,ID\n")
        mock_open().write.assert_any_call("John,Doe,125\n")

    @patch('builtins.input', side_effect=["no"])
    @patch('os.path.isfile', return_value=True)
    # Zmienić nazwę funkcji na bardziej zrozumiałą
    def test_no_addition(self, mock_isfile, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manage_student_file()
            self.assertIn("Operation terminated.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
