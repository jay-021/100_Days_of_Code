# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.

from operator import le


colors = ["white", "black", "green", "red", "blue", "yellow"]
print(type(colors))
print("length of colors is ", len(colors))
print(colors)
# we can add values after creating the list using append method
colors.append("pink")
print(colors)
colors.remove("white")  # to remove specific value
print(colors)

if "black" in colors:       # we can check if value si available in list or not
    print("black is present")
else:
    print("black is absent")

# same rules appy with strings
if "arry" in "Harry":
    print(True)
else:
    print(False)

# all slicing rules are apply same as string

# this all are similar
# print from 0 index to 6 it will print 0th index but not 6th
print(colors[0:6])
print(colors[0:])
print(colors[:6])

# negative slicing
print(colors[-4:-1])  # easy trick: -4 means length -4 same with others
print(colors[len(colors)-4:len(colors)-1])

# jump index [start: end: Jump]
# print from 0 index to 6 with jump on every second element
print(colors[0:6:2])

# List comprehensions are used for creating new lists
#  from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

lst = [i*i for i in range(11)]  # lst create squers of 10 numbers usng loop
print(lst)
lst = [i for i in range(11) if i % 2 == 0]
# it generates new list wtih  numbers using for loop and if condition
print(lst)
