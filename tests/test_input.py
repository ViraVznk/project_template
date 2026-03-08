import os
import tempfile
import unittest

from app.io.input import *


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

    def test_rf_returns_string(self):
        """
        read_file must return type str
        """
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as t:
            t.write("read_file must return type str")
            tmp_path = t.name
        try:
            res = read_file(tmp_path)
            self.assertIsInstance(res, str)
        finally:
            os.remove(tmp_path)

    def test_rf_raises_for_missing_file(self):
        """
        read_file should throw FileNotFoundError if the file does not exist.
        """
        try:
            read_file("/not/found/path/file.txt")
        except FileNotFoundError:
            pass
        else:
            self.fail("I expected an error, but something went wrong.")


class TestReadFilePandas(unittest.TestCase):
    def test_rfp_returns_dataframe(self):
        """
        read_file_pandas should return a pandas DataFrame object.
        """
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv",delete=False, encoding="utf-8") as t:
            t.write("1,Щось\n2,Щось\n3,Щось\n")
            tmp_path = t.name
        try:
            res = read_file_pandas(tmp_path)
            self.assertIsInstance(res, pd.DataFrame)
        finally:
            os.remove(tmp_path)

if __name__ == '__main__':
    unittest.main()
