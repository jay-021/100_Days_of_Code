countries = ("India", "USA", "UK", "Spain", "Argentina", "Nepal")
print(countries)
# we can't change tuple but we can convert into list and then modify it and convert back to tuple
temp = list(countries)
temp.append('Russia')
temp.pop(5)
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(len(countries),countries)


#However, we can directly concatenate two tuples without converting them to list.
countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China",1,2,2,3,2)
southEastAsia = countries + countries2
print(southEastAsia)

# The count() method of Tuple returns the number of times the given element appears in the tuple.
print("count(2): \t",southEastAsia.count(2))
print("First occurance of 2 ", southEastAsia.index(2))  # if value is not available in tuple it'll through you value error
# tuple.index(element, start, end)
print("first occurance of 2 in between 6 to 11 at index ",southEastAsia.index(2,6,11))

# visit this website for more details by harry bhai 
# https://replit.com/@codewithharry/25-Day25-Operations-on-Tuples#main.py