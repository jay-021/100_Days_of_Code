# Functions are block of code which performs a specific task whenever it is called.

def isless(a, b):
    # def is for define and we have to name it and pass the values
    pass
# pass means we will write it in future


def bignum(a, b):
    if a > b:
        print(a, "is greater that", b)
    elif a == b:
        print(a, "and ", b, "both are same")
    else:
        print(b, "is greater that", a)


print(bignum(4, 21))
