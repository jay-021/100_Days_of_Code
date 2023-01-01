data = {'name': 'Jay', 'age': 19, 'study': True, 'online': False}

# The update() method updates the value of the key provided to it
# if the item already exists in the dictionary, else it creates a new key-value pair.
data.update({'name': 'Shubham'})
print(data['name'])
data.update({'clg': 'VU'})
print(data)
bday = {'doy': 2000}
data.update(bday)
print(data)


# Removing items from dictionary:

# The pop() method removes the key-value pair whose key is passed as a parameter.
data.pop('online')
print(data)

# The popitem() method removes the last key-value pair from the dictionary.
data.popitem()
print(data)

# we can also use the del keyword to remove a dictionary item.
del data['study']
print(data)

# If key is not provided, then the del keyword will delete the dictionary entirely.
# del data
# print(data)

# The clear() method removes all the items from the list.

data.clear()
print(data)

# read more here for python 3.10 :- https://docs.python.org/3.10/tutorial/datastructures.html#dictionaries
# read more here for python 3.11 :- https://docs.python.org/3.11/tutorial/datastructures.html#dictionaries
