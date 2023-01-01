# Sets are unordered collection of data items. They store multiple items in a single variable.
# Set items are separated by commas and enclosed within curly brackets {}.
# Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.


# you can do anything with set which is possible with tuple
# look in the output order will be changed
sett = {"shubham", 6.3, 344, 2, 3, 3, 2, True, "_", "Raja"}
print(type(sett))
print(sett)


# if you create empty set like this it will make it dictionary
seaa = {}
print(type(seaa))
seaa = set()
print(type(seaa))

# access the values in set using for loop
for value in sett:
    print(value)
