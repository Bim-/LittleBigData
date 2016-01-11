# -*- coding: utf-8 -*-

# change when file name changes!
from Task3 import word, lundtime
from datetime import *
from matplotlib.pyplot import *
from astral import *

ggl = Astral(GoogleGeocoder)
loc_ss = ggl.geocoder["Södra sandby"]

a = datetime(2015, 3, 1)
b = datetime(2015, 3, 6)

yl = []
xl = []

for i in lundtime:
    if a <= i <= b:
        sun = loc_ss.solar_elevation(i)
        yl.append(sun)
        xl.append(i)
        
plot(xl, yl)