age = int(input("Enter your age : "))
print("Your age is ", age)

'''conditional operators
# >, < , <= ,>=  ,== , !=
print(age>18)
print(age<18)
print(age>=18)
print(age<=18)
print(age==18)
print(age!=18)'''

if (age > 18):
    print('You can drive')
else:
    print("You can not drive")

# Elif
num = int(input("Enter the value of num: "))
if (num < 0):
    print("The num value ", num, "is negeative.")
elif (num == 0):
    print('The num is  zero.')
elif (num == 999):
    print('The num is special.')
else:
    print('The num is positive')

# nested conditions

num = int(input("Enter the value of num: "))
if (num < 0):
    print("The num value ", num, "is negeative.")

elif (num > 0):
    if (num == 1-10):
        print('The num is in between 1 to 10')
    elif (num == 10-20):
        print('The num is in between 10 to 20')
    else:
        print('The num is greater than 20')
else:
    print("The number is zero")
