# -*- coding: utf-8 -*-

from Tasks_1_and_2 import lundtime, counter

# birddict = dict(zip(lundtime, counter))

diff = []
# j has to be equal to counter[0]
j = 70

for i in counter:
    delta = abs(i-j)
    if delta > 8:
        delta = 1
    diff.append(delta)
    j = i


# dictionary of everything. so we can add other stuff(eg sun/weather)
# and access it by date (bird is the..)

word = {lundtime[i]: {'reg': counter[i], 'diff': diff[i]}
        for i in range(len(diff))}
