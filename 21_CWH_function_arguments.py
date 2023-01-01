def average(a=4, b=4):
    # here value of a and b is consisder as a default value
    print("The average is ", ((a+b)/2))


# average()
average(1, 5)
# if  you only pass one value here still it works because it uses  default value


def name(fname, mname="bhai", lname="patel"):
    print("hello", fname, mname, lname)


name("jay")

# variable length argument


def average(*numbers):  # here one * means it'll pass value as a tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ",sum/ len(numbers))
    print(type(numbers))
    return "the average is:", sum/len(numbers)
    # return statement returns the value which we passed


c = average(5, 6, 7, 1)
print(c)
# Keywrd Arbitarary Arguments


def name(**name):  # here double ** means it'll pass value as a dictionary
    print(type(name))
    print("hello", name['fname'], name['mname'], name['lname'])


name(mname='vansh', lname='patel', fname='raj')
