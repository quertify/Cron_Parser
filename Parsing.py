# !/usr/bin/env python3
import sys

class Parsing:
    field_range = [(0,59), (0,23),(1,31),(1,12),(0,6)]
    fields = ["minute", "hour", "day of month", "month", "day of week"]
    special_chars =  [",", "-", "*", "/"]

    def __init__(self, expression):
        self.expression = expression

    # Validate each field in the cron expression for validity
    def __validate_field(self, field, field_range):
        for v in field:
            if v.isdigit():
                continue
            if  v in self.special_chars:
                continue
            else:
                raise ValueError(f"Invalid Character in the field: {field}")
            
        start, end = field_range
        section = field.split(',')
        for sub in section:
            if sub == '*':
                continue
            elif '/' in sub:
                up, down = sub.split('/')
                if not down.isdigit() or int(down) < 0:
                    raise ValueError(f"Invalid split value : {down}")
                if up !='*' and ('-' not in up and not self._validate_range(up, start, end)):
                    raise ValueError(f"Invalid split value of base: {up}")
            elif '-' in sub:
                if not self._validate_range(sub,start,end):
                    raise ValueError(f"Invalid range interval: {sub}")
            elif not sub.isdigit() or not (start <= int(sub) <= end):
                raise ValueError(f"Invalid value, or out of bound: {sub}")

    # Validate ranges within the cron expression field     
    def _validate_range(self,item, start, end):
        if '-' in item:
            low, high = [int(val) for val in item.split('-')]
            return start <=low <= high <= end
        return False

    # This method validates the complete cron expression
    def validate_exp(self):
        vals = self.expression.split()
        if len(vals)!= 6:
            raise ValueError("Error: Invalid cron format, Field count should be 6")
        for i, items in enumerate(vals[:-1]):
            self.__validate_field( items, self.field_range[i])
        return True

    
    # field wise parser in cron expression
    def _parse_field(self, field, field_range):
        values = []
        start = field_range[0]
        end = field_range[1]
        if field == '*':
            values.extend(range(start, end + 1))
        elif ',' in field:
            for item in field.split(','):
                values.extend(self._parse_field(item, field_range))
        elif '/'  in field:
            first, last = field.split('/')
            last = int(last)
            if first == '*':
                first = start
                values.extend(range(first,end+1,last))
            elif '-' in first:
                intvl = [int(val) for val in first.split('-')]
                values.extend(range(intvl[0], intvl[1]+ 1, int(last)))
            else:
                raise ValueError(f'Error: Invalid cron expression {field}')
        elif '-' in field:
            interval = [int(val) for val in field.split('-')]
            values.extend(range(interval[0],interval[-1]+1))
        else:
            values.append(int(field))
        return values

    # Parse the cron expression
    def parse(self):
        self.validate_exp()
        vals = self.expression.split()
        output = []
        for i, val in enumerate(vals[:-1]):
            values = self._parse_field(val, self.field_range[i])
            output.append((self.fields[i], " ".join([str(v) for v in values])))
        output.append(("command", vals[-1]))
        return output

    # Print the parsed output with formatting
    def _print_box(self, output):
        for name, values in output:
            print(f"{name:<14} {values }")
        pass



def main():
    if len(sys.argv) != 2:
        print("Usage: python cronparser.py \"<cron expression>\"")
        return
    try:
        cron_exp = sys.argv[1]
        exp = Parsing(cron_exp)
        p = exp.parse()
        exp._print_box(p)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
