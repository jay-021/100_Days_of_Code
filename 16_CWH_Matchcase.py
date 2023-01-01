# Match case is a same thing like swithch case in other programming language
x = int(input("Enter the number : "))
# x is the variable to match
match x:
    case 0:
        print("X is zero")
    case _ if x != 60:
        print(x, " is not 60.")
    case _ if x > 0:
        print(" case is positive number")
