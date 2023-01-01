'''The isdisjoint() method checks if items of given set are present in another set. 
This method returns False if items are present, else it returns True.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("cities.isdisjoint(cities2) = ", cities.isdisjoint(cities2))

'''The issuperset() method checks if all the items of a particular set are present in the original set. 
It returns True if all the items are present, else it returns False.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Berlin"}
print("cities.issuperset(cities2) = ", cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid", "Kabul"}
print("cities.issuperset(cities3) = ", cities.issuperset(cities3))

'''The issubset() method checks if all the items of the original set are present in the particular set. 
It returns True if all the items are present, else it returns False.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print("cities2.issubset(cities) = ", cities2.issubset(cities))

# If you want to add a single item to the set use the add() method.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print("after cities.add('Helsinki') = ", cities)

'''If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), 
and use the update() method to add it into the existing set.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = ["Las Vegas", "Amsterdam"]
cities.update(cities2)
print("After cities.update(cities2) = ", cities)

'''We can use remove() and discard() methods to remove items form list.
The main difference between remove and discard is that, if we try to delete an item which is not present in set, 
then remove() raises an error, whereas discard() does not raise any error.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print("After cities.remove('Tokyo') = ", cities)
# cities.remove("Surat")
# print("After cities.remove('Surat') = ",cities)

'''pop() method removes the last item of the set but the catch is that we don’t know 
which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print("After cities.pop() = ", cities)
print("Item which is popped ", item)

# You can also check if an item exists in the set or not. using if else
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
if "Surat" in cities:
    print("Surat is in this set")
else:
    print("Surat is not in this set")


# clear() method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print("After cities.clear() = ", cities)


# del is not a method, rather it is a keyword which deletes the set entirely.
del cities
print("After del cities it will raise an name error")
# print("After del cities = ",cities)
