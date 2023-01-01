cities1 = {'List1', 'New York', 'Los Angeles',
        'Vilnius', 'Madrid', 'Kaunas', 'Rome'}
cities2 = {'List2', 'Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Rome', 'Madrid'}


'''   I. union() and update():
The union() and update() methods prints all items that are present in the two sets. 
The union() method returns a new set whereas update() method adds item into the existing set from another set 
'''
# cities = cities1.union(cities2)
# print("union() ",cities)
# print("after union()",cities1,cities2)

# cities1.update(cities2)
# print("update",cities1)
# print("after update ",cities1,cities2)

'''
II. intersection and intersection_update():
The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
'''

# cities1 = {'List1','New York', 'Los Angeles', 'Vilnius', 'Madrid', 'Kaunas', 'Rome'}
# cities2 = {'List2','Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Rome', 'Madrid'}

# cities = cities1.intersection(cities2)
# print("intersection() ",cities)
# print("after intersection() ",cities1,cities2)

# cities1.intersection_update(cities2)
# print("intersection_update() " ,cities1 )
# print("after intersection_update()",cities1,cities2)

'''
III. symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 
The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
'''
# cities1 = {'List1','New York', 'Los Angeles', 'Vilnius', 'Madrid', 'Kaunas', 'Rome'}
# cities2 = {'List2','Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Rome', 'Madrid'}

# cities = cities1.symmetric_difference(cities2)
# print("symmetric_difference() \n",cities)
# print('after symmetric_difference() \n',cities1,cities2)

# cities1.symmetric_difference_update(cities2)
# print("symmetric_difference_update() \n", cities1)
# print('after symmetric_difference_update() \n',cities1,cities2)

'''
IV. difference() and difference_update():
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
'''

# cities1 = {'List1','New York', 'Los Angeles', 'Vilnius', 'Madrid', 'Kaunas', 'Rome'}
# cities2 = {'List2','Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Rome', 'Madrid'}

# cities = cities1.difference(cities2)
# print("difference() \n",cities)
# print('after difference() \n',cities1,cities2)

# cities1.difference_update(cities2)
# print("difference_update() \n", cities1)
# print('after difference_update() \n',cities1,cities2)
