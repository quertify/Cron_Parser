from cronparser.interfaces import ICronPrinter

class DefaultCronPrinter(ICronPrinter):
    def print_box(self, output):
        for name, values in output:
            print(f"{name:<14} {values}")
