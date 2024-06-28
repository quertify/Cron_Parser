import sys
from validators import DefaultCronValidator
from parsers import DefaultCronParser
from schedulers import DefaultCronScheduler
from printers import DefaultCronPrinter
from cron_expression import CronExpression

def main():
    if len(sys.argv) != 2:
        print("Usage: python cronparser.py \"<cron expression>\"")
        return
    try:
        cron_exp = sys.argv[1]

        validator = DefaultCronValidator()
        parser = DefaultCronParser()
        scheduler = DefaultCronScheduler()
        printer = DefaultCronPrinter()

        cron_expression = CronExpression(cron_exp, validator, parser, scheduler, printer)
        parsed_output = cron_expression.parse()
        cron_expression.print(parsed_output)
        next_times = cron_expression.get_next_iterations(5, parsed_output, '2024-12-31 00:58:00')
        print(next_times)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()