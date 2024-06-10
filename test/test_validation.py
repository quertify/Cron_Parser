import unittest
from Parsing import Parsing

class TestValidation(unittest.TestCase):

    def test_valid_value_expression(self):
        testcase1 = Parsing("0 * * * * /user/command")
        expected_output = [
                ("minute", "0"),
                ("hour", "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23"),
                ("day of month", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"),
                ("month", "1 2 3 4 5 6 7 8 9 10 11 12"),
                ("day of week", "0 1 2 3 4 5 6"),
                ("command", "/user/command")
            ]
        self.assertEqual(testcase1.parse(), expected_output)

    def test_invalid_character(self):
        with self.assertRaisesRegex(ValueError, r"Invalid Character in the field: @1-5"):
            Parsing("*/15 0 1,15 * @1-5 /usr/bin/command").validate_exp()

    def test_invalid_step(self):
        with self.assertRaisesRegex(ValueError, r"Invalid split value : -15"):
            Parsing("*/-15 0 1,15 * 1-5 /usr/bin/command").validate_exp()

    def test_value_out_of_range(self):
        with self.assertRaisesRegex(ValueError, r"Invalid range interval: 1-40"):
            Parsing("*/15 0 1-40 * 1-5 /usr/bin/command").validate_exp()

    def test_missing_fields(self):
        with self.assertRaisesRegex(ValueError, r"Error: Invalid cron format, Field count should be 6"):
            Parsing("0 * * * *").validate_exp()

    def test_empty_expression(self):
        with self.assertRaisesRegex(ValueError,  r"Error: Invalid cron format, Field count should be 6" ):
            Parsing("0 0 * * ").validate_exp()
if __name__ == "__main__":
    unittest.main(verbosity=2)
