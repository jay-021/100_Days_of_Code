# time = int(input("Enter the time in 24 hr format.  :  "))


import time
timestemp = time.strftime('hr:min:sec: \t''%H:%M:%S')
print(timestemp)
timestemp = time.strftime('hr''\t%H')
print(timestemp)
timestemp = time.strftime('min\t''%M')
print(timestemp)
timestemp = time.strftime('sec''\t%S')
print(timestemp)

timestemp = int(time.strftime('%H'))

if (timestemp == 21 - 24 & timestemp < 8):
    print("Good night sir")
elif (timestemp >= 17):
    print("Good evening sir")
elif (timestemp >= 12):
    print("Good afternoon sir")
else:
    print("Good Morning sir")
