import unittest
from cronparser.cron_expression import CronExpression
from cronparser.validators import DefaultCronValidator
from cronparser.parsers import DefaultCronParser
from cronparser.schedulers import DefaultCronScheduler
from cronparser.printers import DefaultCronPrinter

class TestDefaultCronValidator(unittest.TestCase):
    def setUp(self):
        self.validator = DefaultCronValidator()
        self.parser = DefaultCronParser()
        self.scheduler = DefaultCronScheduler()
        self.printer = DefaultCronPrinter()

    def test_valid_cron_expression(self):
        cron_exp = "*/15 0 1,15 * 1-5 /usr/bin/find"
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        validate_output = cron_expression.validate()
        self.assertTrue(validate_output)

    def test_invalid_character(self):
        cron_exp = "*/15 0 1,15 * @1-5 /usr/bin/find"
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        with self.assertRaises(ValueError):
            cron_expression.validate()

    def test_invalid_step(self):
        cron_exp = "*/-15 0 1,15 * 1-5 /usr/bin/find"
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        with self.assertRaises(ValueError):
            cron_expression.validate()

    def test_value_out_of_range(self):
        cron_exp = "*/15 0 1-40 * 1-5 /usr/bin/find"
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        with self.assertRaises(ValueError, msg="Invalid range interval: 1-40"):
            cron_expression.validate()

    def test_missing_fields(self):
        cron_exp = "0 * * * *"
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        with self.assertRaises(ValueError, msg="Invalid cron format: Must have 6 or 7 fields"):
            cron_expression.validate()

    def test_empty_expression(self):
        cron_exp = "0 0 * * "
        cron_expression = CronExpression(cron_exp, self.validator, self.parser, self.scheduler, self.printer)
        with self.assertRaises(ValueError, msg="Invalid cron format: Must have 6 or 7 fields"):
            cron_expression.validate()

if __name__ == "__main__":
    unittest.main(verbosity=2)
