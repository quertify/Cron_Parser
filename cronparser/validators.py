from constants import CronConstants
from interfaces import ICronValidator

class DefaultCronValidator(ICronValidator):
    def __init__(self):
        self.special_chars = CronConstants.SPECIAL_CHARS
        self.months_dict = CronConstants.MONTHS_DICT
        self.weeks_dict = CronConstants.WEEKS_DICT
        self.field_range = CronConstants.FIELD_RANGE

    def validate(self, field, field_range):
        start, end = field_range
        section = field.split(',')
        for c in field:
            if c not in self.special_chars and not c.isdigit() and not c.isalpha():
                raise ValueError(f"Invalid character in the field: {field}")
        for sub in section:
            if sub == '*':
                continue
            elif '/' in sub:
                self._validate_slash(sub, start, end)
            elif '-' in sub:
                self._validate_dash(sub, start, end)
            elif sub.isalpha():
                self._validate_alpha(sub, field_range)
            elif not sub.isdigit() or not (start <= int(sub) <= end):
                raise ValueError(f"Invalid value, or out of bound: {sub}")

    def _validate_slash(self, sub, start, end):
        up, down = sub.split('/')
        if not down.isdigit() or int(down) < 0:
            raise ValueError(f"Invalid split value: {down}")
        if up != '*' and ('-' not in up and not self._validate_range(up, start, end)):
            raise ValueError(f"Invalid split value of base: {up}")

    def _validate_dash(self, sub, start, end):
        if not self._validate_range(sub, start, end):
            raise ValueError(f"Invalid range interval: {sub}")

    def _validate_alpha(self, sub, field_range):
        if sub.upper() in self.months_dict:
            if field_range == self.field_range[3]:
                return
            else:
                raise ValueError(f"Invalid month name in wrong field: {sub}")
        if sub.upper() in self.weeks_dict:
            if field_range == self.field_range[4]:
                return
            else:
                raise ValueError(f"Invalid week name in wrong field: {sub}")
        else:
            raise ValueError(f"Invalid character in the field: {sub}")

    def _validate_range(self, item, start, end):
        if '-' in item:
            low, high = [val for val in item.split('-')]
            if low.isdigit() and high.isdigit():
                return start <= int(low) <= end and start <= int(high) <= end
            elif low in self.months_dict and high in self.months_dict:
                return start <= self.months_dict[low] <= end and start <= self.months_dict[high] <= end
            elif low in self.weeks_dict and high in self.weeks_dict:
                return start <= self.weeks_dict[low] <= end and start <= self.weeks_dict[high] <= end
        return False
