""" The enumerate function is a built-in function in Python that allows you to loop over a 
sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. """

# use case (basic) : if you want to print values of list tuple string with index then how do you do that like this 
names = ["Jay","Shubham","Raj","Kathan","Muslim","Salam","Aish"]
""" 
index = 0
for name in names:
    print(index,name)
    if index == 2:
        print("He bought a car.")
    index += 1 """

# but here how you can do this simply by using enumerate function


for index, name in enumerate(names):
    print(index,name)
    if index == 2:
        print("He bought a car.")

# by default it start with index 0 but we can also start this with 1 like if i want to print that line before raj's name 

for index, name in enumerate(names,start=1):
    print(index,name)
    if index == 2:
        print("He bought a car.")

# You can use this same with strings as well as tuples