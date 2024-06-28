class CronConstants:
    SPECIAL_CHARS = [",", "-", "*", "/"]
    MONTHS_DICT = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}
    WEEKS_DICT = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
    FIELD_RANGE = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 6), (1990, 2090)]
    FIELDS = ["minute", "hour", "day of month", "month", "day of week", "year"]
