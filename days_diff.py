#!/usr/bin/python
from datetime import date

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    new_date1 = date(date1[0], date1[1], date1[2])
    new_date2 = date(date2[0], date2[1], date2[2])
    delta = abs((new_date2-new_date1).days)
    print delta
    return delta

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
