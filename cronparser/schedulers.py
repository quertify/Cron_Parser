from datetime import datetime, timedelta
from cronparser.interfaces import ICronScheduler

class DefaultCronScheduler(ICronScheduler):
    def next_iterations(self, n, output, given_time):
        counter = {}
        for name, values in output[:5]:
            counter[name] = set(int(v) for v in values.split())
        curr = datetime.strptime(given_time, '%Y-%m-%d %H:%M:%S')
        res = []
        while len(res) < n:
            if (curr.minute in counter["minute"]) and (curr.hour in counter["hour"]) \
                and (curr.day in counter["day of month"]) and (curr.month in counter["month"]) \
                and (curr.weekday() + 1 in counter["day of week"]):
                res.append(curr.strftime("%Y-%m-%d %H:%M:%S"))
            curr += timedelta(minutes=1)
        return res
