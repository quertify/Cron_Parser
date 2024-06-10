#Unit test file for Cron parser
import unittest
from Parsing import Parsing

class TestParsing(unittest.TestCase):
    def test_parse_valid_expression(self):
    # Test that the parse method correctly parses a valid cron expression
        testcase1 = Parsing("*/15 0 1,15 * 1-5 /usr/bin/find")
        expected_output = [
            ("minute", "0 15 30 45"),
            ("hour", "0"),
            ("day of month", "1 15"),
            ("month", "1 2 3 4 5 6 7 8 9 10 11 12"),
            ("day of week", "1 2 3 4 5"),
            ("command", "/usr/bin/find")
        ]
        self.assertEqual(testcase1.parse(), expected_output)

    def test_invalid_expression(self):
        testcase2 = Parsing("* * * * *")
        with self.assertRaises(ValueError):
            testcase2.parse()

    
    # Testing the ranges for all the fields

    def test_parse_range_start_expression(self):
    # Test that the parse method correctly parses a valid cron expression
        testcase3 = Parsing("0 0 1 1 0 /user/parse/pin")
        expected_output = [
            ("minute", "0"),
            ("hour", "0"),
            ("day of month", "1"),
            ("month", "1"),
            ("day of week", "0"),
            ("command", "/user/parse/pin")
        ]
        self.assertEqual(testcase3.parse(), expected_output)

    def test_parse_range_end_expression(self):
        testcase4 = Parsing("59 23 31 12 6 /user/parse/pin")
        expected_output = [
            ("minute", "59"),
            ("hour", "23"),
            ("day of month", "31"),
            ("month", "12"),
            ("day of week", "6"),
            ("command", "/user/parse/pin")
        ]
        self.assertEqual(testcase4.parse(), expected_output)
    def test_invalid_range_expression(self):
        testcase5 = Parsing("-1 24 32 13 7 command")
        with self.assertRaises(ValueError):
            testcase5.parse()

    def test_valid_cron_expression_with_steps(self):
        testcase6 = Parsing("0 9/2 * * 1-5 /usr/bin/purge-temps")
        with self.assertRaises(ValueError):
            testcase6.parse()


if __name__ == "__main__":
    unittest.main(verbosity=2)
              