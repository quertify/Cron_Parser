from cronparser.constants import CronConstants
from cronparser.interfaces import ICronParser

class DefaultCronParser(ICronParser):
    def __init__(self):
        self.special_chars = CronConstants.SPECIAL_CHARS
        self.months_dict = CronConstants.MONTHS_DICT
        self.weeks_dict = CronConstants.WEEKS_DICT
        self.field_range = CronConstants.FIELD_RANGE

    def parse(self, expression):
        vals = expression.split()
        output = []
        for i, val in enumerate(vals[:-1]):
            values = self._parse_field(val, self.field_range[i])
            output.append([CronConstants.FIELDS[i], " ".join([str(v) for v in values])])
        output.append(["command", vals[-1]])
        return output

    def _parse_field(self, field, field_range):
        values = []
        start, end = field_range[0], field_range[1]
        if field == '*':
            values.extend(range(start, end + 1))
        elif ',' in field:
            self._parse_comma(field, values, field_range)
        elif '/' in field:
            self._parse_slash(field, values, start, end)
        elif '-' in field:
            self._parse_dash(field, values, field_range)
        elif field in self.months_dict:
            values.append(self.months_dict[field])
        elif field in self.weeks_dict:
            values.append(self.weeks_dict[field])
        else:
            values.append(int(field))
        return values

    def _parse_comma(self, field, values, field_range):
        for item in field.split(','):
            values.extend(self._parse_field(item, field_range))

    def _parse_slash(self, field, values, start, end):
        first, last = field.split('/')
        last = int(last)
        if first == '*':
            first = start
            values.extend(range(first, end + 1, last))
        elif '-' in first:
            intvl = [int(val) for val in first.split('-')]
            values.extend(range(intvl[0], intvl[1] + 1, last))
        else:
            raise ValueError(f"Error: Invalid cron expression {field}")

    def _parse_dash(self, field, values, field_range):
        start, end = field_range
        interval = [val for val in field.split('-')]
        if interval[0] in self.months_dict and interval[1] in self.months_dict:
            interval[0] = self.months_dict[interval[0]]
            interval[1] = self.months_dict[interval[1]]
        elif interval[0] in self.weeks_dict and interval[1] in self.weeks_dict:
            interval[0] = self.weeks_dict[interval[0]]
            interval[1] = self.weeks_dict[interval[1]]
        interval[0], interval[1] = int(interval[0]), int(interval[1])
        if interval[0] <= interval[1]:
            values.extend(range(interval[0], interval[1] + 1))
        else:
            values.extend(self._generate_cyclic_order(interval[0], interval[1], end, start))

    def _generate_cyclic_order(self, start, end, max_val, min_val):
        if start <= end:
            return list(range(start, end + 1))
        return list(range(start, max_val + 1)) + list(range(min_val, end + 1))
