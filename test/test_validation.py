import unittest
from unittest.mock import MagicMock
from cronparser.cron_expression import CronExpression
from cronparser.validators import DefaultCronValidator
from cronparser.parsers import DefaultCronParser
from cronparser.schedulers import DefaultCronScheduler
from cronparser.printers import DefaultCronPrinter

class TestCronExpressionValidation(unittest.TestCase):

    def setUp(self):
        # Create a mock for DefaultCronValidator
        self.validator = DefaultCronValidator()
        self.parser = DefaultCronParser()
        self.scheduler = DefaultCronScheduler()
        self.printer = DefaultCronPrinter()
        self.validator.validate = MagicMock(return_value=True)  # Mock the validate method

        # Create mocks for other components (parser, scheduler, printer)
        self.parser = MagicMock()

    def test_valid_cron_expression(self):
        # Set up a valid cron expression
        cron_exp = "*/15 * * * * /user/command"

        # Create CronExpression instance with mocks

        # Assert that validate() method of the validator was called once with cron_exp
        self.validator.validate.assert_called_once_with(cron_exp)

    def test_invalid_cron_expression(self):
        # Set up an invalid cron expression
        invalid_cron_exp = "*/-15 0 1,15 * 1-5 /usr/bin/command"

        # Mock the validator to raise a ValueError when validate() is called
        self.validator.validate = MagicMock(side_effect=ValueError("Invalid cron expression"))

        # Create CronExpression instance with mocks
        cron_expression = CronExpression(invalid_cron_exp, self.validator, self.parser, self.scheduler, self.printer)

        # Expect a ValueError to be raised when parse() method is called
        with self.assertRaises(ValueError):
            cron_expression.parse()

    def test_empty_expression(self):
        # Test an empty cron expression
        empty_exp = ""

        # Mock the validator to raise a ValueError when validate() is called with empty_exp
        self.validator.validate = MagicMock(side_effect=ValueError("Invalid cron expression"))

        # Create CronExpression instance with mocks
        cron_expression = CronExpression(empty_exp, self.validator, self.parser, self.scheduler, self.printer)

        # Expect a ValueError to be raised when parse() method is called
        with self.assertRaises(ValueError):
            cron_expression.parse()

    def test_missing_command(self):
        # Test a cron expression missing the command part
        exp_without_command = "0 * * * *"

        # Mock the validator to raise a ValueError when validate() is called with exp_without_command
        self.validator.validate = MagicMock(side_effect=ValueError("Invalid cron expression"))

        # Create CronExpression instance with mocks
        cron_expression = CronExpression(exp_without_command, self.validator, self.parser, self.scheduler, self.printer)

        # Expect a ValueError to be raised when parse() method is called
        with self.assertRaises(ValueError):
            cron_expression.parse()

    def test_invalid_field_value(self):
        # Test a cron expression with an invalid field value
        exp_with_invalid_value = "*/15 0 1-40 * 1-5 /usr/bin/command"

        # Mock the validator to raise a ValueError when validate() is called with exp_with_invalid_value
        self.validator.validate = MagicMock(side_effect=ValueError("Invalid cron expression"))

        # Create CronExpression instance with mocks
        cron_expression = CronExpression(exp_with_invalid_value, self.validator, self.parser, self.scheduler, self.printer)

        # Expect a ValueError to be raised when parse() method is called
        with self.assertRaises(ValueError):
            cron_expression.parse()

if __name__ == "__main__":
    unittest.main(verbosity=2)
