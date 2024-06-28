import unittest
from unittest.mock import MagicMock
from cronparser.cron_expression import CronExpression
from cronparser.validators import DefaultCronValidator
from cronparser.parsers import DefaultCronParser
from cronparser.schedulers import DefaultCronScheduler
from cronparser.printers import DefaultCronPrinter

class TestCronExpressionParsing(unittest.TestCase):
    def setUp(self):
        # Create mock objects for the components (validator, parser, scheduler, printer)
        self.validator = DefaultCronValidator()
        self.parser = DefaultCronParser()
        self.scheduler = DefaultCronScheduler()
        self.printer = DefaultCronPrinter()

    def test_parse_valid_expression(self):
        # Test parsing a valid cron expression
        cron_exp = "*/15 0 1,15 * 1-5 /usr/bin/find"
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        
        # Mock the parse method of parser to return expected output
        expected_output = [
            ("minute", "0 15 30 45"),
            ("hour", "0"),
            ("day of month", "1 15"),
            ("month", "1 2 3 4 5 6 7 8 9 10 11 12"),
            ("day of week", "1 2 3 4 5"),
            ("command", "/usr/bin/find")
        ]
        self.parser.parse = MagicMock(return_value=expected_output)

        # Call parse() method of CronExpression and assert output
        parsed_output = cron_expression.parse()
        self.assertEqual(parsed_output, expected_output)

    def test_invalid_expression(self):
        # Test parsing an invalid cron expression
        invalid_cron_exp = "* * * * *"
        cron_expression = CronExpression(invalid_cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        
        # Mock the parser to raise a ValueError when parse() is called
        self.parser.parse = MagicMock(side_effect=ValueError("Invalid cron expression"))

        # Expect a ValueError to be raised when parse() method is called
        with self.assertRaises(ValueError):
            cron_expression.parse()

if __name__ == "__main__":
    unittest.main(verbosity=2)