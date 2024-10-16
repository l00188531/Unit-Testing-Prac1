import unittest
from date_utils import is_valid_date

class TestDateUtils(unittest.TestCase):

    def test_valid_date_in_range(self):
        # Valid date within range
        self.assertTrue(is_valid_date("2022-05-15"))

    def test_valid_date_out_of_range(self):
        # Valid date but out of range
        self.assertFalse(is_valid_date("2024-01-01"))

    def test_invalid_date_format(self):
        # Invalid date format
        self.assertFalse(is_valid_date("15-05-2022"))
    
    def test_edge_case_start_date(self):
        # Valid date exactly on the start date
        self.assertTrue(is_valid_date("2020-01-01"))


if __name__ == '__main__':
    unittest.main()
