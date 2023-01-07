# result = value_if_true if condition else value_if_false
a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
print(a,"is big") if a>b else print("Both are equal") if a==b else print(b, "is big")

# you must have add else part .like this else "" if it's empty
# print("Both are not equal") if a!=b else ""

""" The shorthand syntax can be a convenient way to write simple if-else statements, 
especially when you want to assign a value to a variable based on a condition. """

c = a+b if a!=b else ""
print("sum = ",c)

# here we assign value to c based on condition 