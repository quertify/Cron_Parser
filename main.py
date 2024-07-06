import sys
from datetime import datetime
from cronparser.validators import DefaultCronValidator
from cronparser.parsers import DefaultCronParser
from cronparser.schedulers import DefaultCronScheduler
from cronparser.printers import DefaultCronPrinter
from cronparser.cron_expression import CronExpression

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py \"<cron expression>\"")
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

        # Let's take next 5 iterations; time should be either provided by user or take 'now' as time
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        next_times = cron_expression.get_next_iterations(5, parsed_output, now)
        for next_time in next_times:
            print(f"Next cron iteration would be at: {next_time}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
