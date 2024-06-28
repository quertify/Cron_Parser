from interfaces import ICronValidator, ICronParser, ICronScheduler, ICronPrinter

class CronExpression:
    def __init__(self, expression, validator: ICronValidator, parser: ICronParser, scheduler: ICronScheduler, printer: ICronPrinter):
        self.expression = expression
        self.validator = validator
        self.parser = parser
        self.scheduler = scheduler
        self.printer = printer

    def validate(self):
        vals = self.expression.split()
        for i, items in enumerate(vals[:-1]):
            self.validator.validate(items, self.validator.field_range[i])
        return True

    def parse(self):
        self.validate()
        return self.parser.parse(self.expression)

    def print(self, output):
        self.printer.print_box(output)

    def get_next_iterations(self, n, output, given_time):
        return self.scheduler.next_iterations(n, output, given_time)
