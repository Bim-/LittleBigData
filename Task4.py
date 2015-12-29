# -*- coding: utf-8 -*-

# change when file name changes!
from Task3 import word, lundtime
from datetime import *
from matplotlib.pyplot import *

"""
1. Run this file

in ipython console do the following:

2. Make a start-date, and end-date
  - do this with: a = datetime(somedate) b = datetime(some other date)

3. try: userplot(a, b, 'month') or 'day' or whatever

4. enjoy how the faboulus colors suddenly appear on the screen

"""

# intervals for plot. total per hour, day...


def interval(timeUnit):
    if timeUnit not in {'month', 'week', 'day', 'hour'}:
        raise Exception("interval must be 'month', 'week', 'day' or 'hour'")
    period = timeUnit

    totaldict = {}
    k_time = set()

    # import datetime differently in mattias task 1 2 (done)
    prev = datetime(1984, 12, 2)

    for k in lundtime:

        if k.month == prev.month and (period is 'month' or (
            k.day == prev.day and (period is 'day' or (
                k.hour == prev.hour and period is 'hour')))):

            k_time.add(k)
            k_time.add(prev)

        elif len(k_time) > 0:
            # would be nice to change prev to prev.period (and useful for plot)
            totaldict[prev]\
                = {'{}total'.format(period): sum(word[i]['diff'] for i in k_time)}

            k_time.clear()

        prev = k

    totaldict[prev]\
        = {'{}total'.format(period): sum(word[i]['diff'] for i in k_time)}

    return totaldict


# generating plot values. needs some tweaking. i think we could ask
# for values in a user dialog and then call this function.


def userplot(start, end, Interval):

    timePeriod = interval(Interval)

    yl = []
    xl = []

    for time in timePeriod:
        if start <= time <= end:
            yl.append(timePeriod[time]['{}total'.format(Interval)])
            xl.append(time)

    bar(xl, yl)

    return show()
