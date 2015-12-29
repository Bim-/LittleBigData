from datetime import *

bfile = open('birdtext.txt','r') # Note: I changed the name of the file!
readall = bfile.readlines()
date_time = []  # I need the underscore since I've imported the method datetime for later computations.
counter = []
for line in readall:
    lsp = line.split('   ') # 3 spacebars indicated in the split (there should be 4 but I realised that some
                            # error lines only have 3 spaces. Now those problematic lines won't cause trouble).
    date_time.append(lsp[0])
    counter.append(int(lsp[1])) # making the counter an integer eliminates the '/n' and eventual extra ' '.
print(date_time[1])     # returns 2015-01-25 14:08:05.036915

'''
For Task 2 we need the datetime module, this makes arithmetics with dates and time possible.
Since our datetime objects are present as strings in date_time list, we need the code in line 29 to make
computations with timedelta possible (this particular command specifies the time we want to add).
'''

lundtime = []
for i in range(len(date_time)):
    lundtime.append(datetime.strptime(date_time[i],"%Y-%m-%d %H:%M:%S.%f") + timedelta(hours=1))
print(lundtime[1])      # returns 2015-01-25 15:08:05.036915 , as expected (UTC + 1).
