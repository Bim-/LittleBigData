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


# intervals for plot. total per hour, day...


def interval(period, timeUnit):
    if timeUnit not in {'month', 'day', 'hour'}:
        raise Exception("interval must be 'month', 'day' or 'hour'")

    totaldict = {}
    k_time = set()

    # import datetime differently in mattias task 1 2 (done)

    prev = datetime(1984, 12, 2)  # we need to have a month/week/day to make the following fork.

    # the year doesn't matter since we're aways talking about 2015.
    for k in lundtime:

        if k.month == prev.month and (timeUnit is 'month' or (
            k.day == prev.day and (timeUnit is 'day' or (
                k.hour == prev.hour and timeUnit is 'hour')))):

            k_time.add(k)
            k_time.add(prev)

        elif len(k_time) > 0:
            # would be nice to change prev to prev.timeUnit (and useful for plot)
            totaldict[prev]\
                = {'{}total'.format(timeUnit): sum(word[i]['diff'] for i in k_time)}

            k_time.clear()

        prev = k

# Need to add the last k since the program since the forloop has been exhausted.
# (It doesn't know the day is over/this is the last line of information).

    totaldict[prev]\
        = {'{}total'.format(timeUnit): sum(word[i]['diff'] for i in k_time)}

    return totaldict


def userplot(start, end, Interval):

    period = []
    for time in lundtime:
        if start <= time <= end:
            period.append(time)

    timePeriod = interval(period, Interval)

    yl = []
    xl = []

    for time in timePeriod:
        if start <= time <= end:
            yl.append(timePeriod[time]['{}total'.format(Interval)])
            xl.append(time)

    if Interval == 'hour':
        intv = 0.02
    elif Interval == 'day':
        intv = 0.2
    else:
        intv = 2
    bar(xl, yl, width=intv)

    return show()
