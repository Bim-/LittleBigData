# -*- coding: utf-8 -*-

# change when file name changes!
from Task3 import word, lundtime
from datetime import *
from matplotlib.pyplot import *
from astral import *

ggl = Astral(GoogleGeocoder)
loc_ss = ggl.geocoder["Södra sandby"]


def interval(period, timeUnit):
    if timeUnit not in {'month', 'day', 'hour'}:
        raise Exception("interval must be 'month', 'day' or 'hour'")

    totaldict = {}
    k_time = set()

    # import datetime differently in mattias task 1 2 (done)

    prev = period[0] + timedelta(32)
    
    # the year doesn't matter since we're aways talking about 2015.
    for Next in period:

        if Next.month == prev.month and (timeUnit is 'month' or (
            Next.day == prev.day and (timeUnit is 'day' or (
                Next.hour == prev.hour and timeUnit is 'hour')))):

            k_time.add(Next)
            k_time.add(prev)

        elif len(k_time) > 0:
            # would be nice to change prev to prev.timeUnit (and useful for plot)
            totaldict[prev]\
                = {'{}total'.format(timeUnit): sum(word[i]['diff'] for i in k_time), \
                'sun': loc_ss.solar_elevation(prev)}


            k_time.clear()

        prev = Next

# Need to add the last k since the forloop has been exhausted.
# (It doesn't know the day is over/this is the last line of information).

    totaldict[prev]\
        = {'{}total'.format(timeUnit): sum(word[i]['diff'] for i in k_time), \
        'sun': loc_ss.solar_elevation(prev)}


    return totaldict


def userplot(start, end, Interval):

    period = []
    for time in lundtime:
        if start <= time <= end:
            period.append(time)

    timePeriod = interval(period, Interval)

    yl = []
    xl = []
    ysun = []
    xsun = []

    for time in timePeriod:
            yl.append(timePeriod[time]['{}total'.format(Interval)])
            xl.append(time)
            ysun.append(timePeriod[time]['sun'])
            xsun.append(time)           
            '''sunelev = timePeriod[time]['sun']
            if sunelev > -10.0:
                ysun.append(sunelev)
            else:
                ysun.append(-10.0)'''            

    if Interval == 'hour':
        intv = 0.02
    elif Interval == 'day':
        intv = 0.2
    else:
        intv = 3
    bar(xl, yl, width=intv)
    bar(xl, ysun, color='pink', alpha=0.4,  width=intv)

    show()
