# len(str) use for finding length of string
fruite = "Mango"
print("length of mango is", len(fruite))

# Slicing
lang = "Python"
print("length of python is", len(lang))

# this all are similar
print(lang[0:6])  # print from 0 index to 6 it will print 0th index but not 6th
print(lang[0:])
print(lang[:6])

# negative slicing
print(lang[-4:-1])  # easy trick: -4 means length -4 same with others
print(lang[len(lang)-4:len(lang)-1])

# jump index [start: end: Jump]
print(lang[0:6:2])  # print from 0 index to 6 with jump on every second element
