import os
import tempfile
import unittest

from app.io.input import read_file


class TestReadFile(unittest.TestCase):
    def test_rf_returns_correct_content(self):
        """
        read_file return the exact text written to the file.
        """
        expected = "read_file return the exact text written to the file.\nest_read_file_returns_correct_content"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as t:
            t.write(expected)
            t_path = t.name
        try:
            res = read_file(t_path)
            self.assertEqual(res, expected)
        finally:
            os.remove(t_path)


if __name__ == '__main__':
    unittest.main()
