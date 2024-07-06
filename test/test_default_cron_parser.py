import unittest
from cronparser.parsers import DefaultCronParser

class TestDefaultCronParser(unittest.TestCase):
    def setUp(self):
        self.parser = DefaultCronParser()

    def test_parse_valid_expression(self):
        cron_exp = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expected_output = [
            ["minute", "0 15 30 45"],
            ["hour", "0"],
            ["day of month", "1 15"],
            ["month", "1 2 3 4 5 6 7 8 9 10 11 12"],
            ["day of week", "1 2 3 4 5"],
            ["command", "/usr/bin/find"]
        ]
        parsed_output = self.parser.parse(cron_exp)
        self.assertEqual(parsed_output, expected_output)

    def test_parse_range_start_expression(self):
        cron_exp = "0 0 1 1 0 /user/parse/pin"
        expected_output = [
            ["minute", "0"],
            ["hour", "0"],
            ["day of month", "1"],
            ["month", "1"],
            ["day of week", "0"],
            ["command", "/user/parse/pin"]
        ]
        parsed_output = self.parser.parse(cron_exp)
        self.assertEqual(parsed_output, expected_output)

    def test_parse_range_end_expression(self):
        cron_exp = "59 23 31 12 6 /user/parse/pin"
        expected_output = [
            ["minute", "59"],
            ["hour", "23"],
            ["day of month", "31"],
            ["month", "12"],
            ["day of week", "6"],
            ["command", "/user/parse/pin"]
        ]
        parsed_output = self.parser.parse(cron_exp)
        self.assertEqual(parsed_output, expected_output)

    def test_invalid_range_expression(self):
        cron_exp = "-1 24 32 13 7 /user/parse/pin"
        with self.assertRaises(ValueError):
            self.parser.parse(cron_exp)

    def test_valid_cron_expression_with_steps(self):
        cron_exp = "0 9/2 * * 1-5 /usr/bin/purge-temps"
        with self.assertRaises(ValueError):
            self.parser.parse(cron_exp)

if __name__ == "__main__":
    unittest.main(verbosity=2)
