import unittest
from unittest.mock import patch, mock_open
import csv

class TestExportStudentsCSV(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_export_students_csv(self, mock_open):
        from import_eksport_files.py import export_students_csv
        students = [{'name': 'John', 'present': True}, {'name': 'Jane', 'present': False}]
        export_students_csv(students, "output.csv")
        mock_open.assert_called_with("output.csv", mode='w', newline='')
        handle = mock_open()
        writer = csv.writer(handle)
        writer.writerow.assert_any_call(['Name', 'Present'])
        writer.writerow.assert_any_call(['John', True])


if __name__ == '__main__':
    unittest.main()
