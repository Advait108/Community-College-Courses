import unittest
from finalassignment import DataSet


class TestCC(unittest.TestCase):

    def test_correct_lines_loaded(self):
        test1 = DataSet()
        test1.load_file()
        self.assertEqual(6147, len(test1._data[0]))


if __name__ == "__main__":
    unittest.main()