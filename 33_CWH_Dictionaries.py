'''Dictionaries are ordered collection of data items. They store multiple items in a single variable. 
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.'''

dicti = {'name': 'Jay', 'age': 19, 'study': True, 'online': False}

print(dicti)

'''I. Accessing single values:
Values in a dictionary can be accessed using keys. 
We can access dictionary values by mentioning keys either in square brackets or by using get method.'''

print(dicti['age'])  # if item is not available then it will through error
print(dicti.get('name'))

'''II. Accessing multiple values:
We can print all the values in the dictionary using values() method.'''

print(dicti.values())

for key in dicti.keys():
    print(f"The value of {key} is {dicti[key]}")

'''III. Accessing keys:
We can print all the keys in the dictionary using keys() method.'''

print(dicti.keys())

'''IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.'''

print(dicti.items())

for key, value in dicti.items():
    print(f"The value of {key} is {value}")  # same thing
