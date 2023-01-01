# Recursion is the process of defining something in terms of itself.
# In Python, we know that a function can call other functions.
# It is even possible for the function to call itself. These types of construct are termed as recursive functions.

def factorial(num):
    '''This function use recursion to evaluate the factorial of given number'''
    if (num == 1):
        return 1
    else:
        return num * factorial(num - 1)


num = (int(input("Enter the number: ")))
print("factorial of", num, 'is : ', factorial(num))


def fibonacci(num):
    '''This function use recursion to evaluate the fibonacci sequence of given number'''
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num - 2)


print("fibonacci sequence of", num, 'is : ', fibonacci(num))
