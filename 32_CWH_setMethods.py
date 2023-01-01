cities1 = {'New York', 'Los Angeles', 'Vilnius', 'Madrid', 'Kaunas', 'Rome'}
cities2 = {'Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Rome', 'Madrid'}


'''   I. union() and update():
The union() and update() methods prints all items that are present in the two sets. 
The union() method returns a new set whereas update() method adds item into the existing set from another set 
'''

print("union() ",cities1.union(cities2))
print("after union()",cities2,cities1)
print("update",cities1.update(cities2))
print("after update ",cities2,cities1) 

'''
II. intersection and intersection_update():
The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
'''

cities1 = {'New York', 'Los Angeles', 'Vilnius', 'Madrid', 'Kaunas', 'Rome'}
cities2 = {'Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Rome', 'Madrid'}