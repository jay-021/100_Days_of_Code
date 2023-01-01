#  Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.

countries = ("India", "USA", "UK", "Spain", "Argentina", "Nepal")
# we can't change this tUple in future if you try it you'll get error
# countries.apend("Pak")  # try this
# countries [1] = ("UAE")
print(type(countries), countries)

# if you want to create tuple of one element you need to add extra coma after value
# fi you don't add coma python understad that as a normal variable
city = ("Las Vegas")
print(type(city), city)
city = ("Las Vegas",)
print(type(city), city)

# we can check the value is present in tuple or not
if "USA" in countries:
    print(True)
else:
    print(False)


# this all are similar
# print from 0 index to 6 it will print 0th index but not 6th
print(countries[0:6])
print(countries[0:])
print(countries[:6])

# negative slicing
print(countries[-4:-1])  # easy trick: -4 means length -4 same with others
print(countries[len(countries)-4:len(countries)-1])

# jump index [start: end: Jump]
# print from 0 index to 6 with jump on every second element
print(countries[0:6:2])


# visit this website for more details by harry bhai 
# https://replit.com/@codewithharry/24-Day24-Introduction-to-Tuples#.tutorial/02-tuple_indexes.md