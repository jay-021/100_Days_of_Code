# we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
""" Syntax
class CustomError(Exception):
    # code ...
    pass

try:
    # code ...

except CustomError:
    # code... """

""" quick quiz : make a program in that if you enter the value greater than 9 or less than 4 than it 
    raise an ValueError but if you enter quit then it will not raise any kind of error . """
try :
    a = input("Enter the number between 4 to 9 : ")
    if a.lower() == "quit":
        print("quitted")
    else:
        b = int(a)
        if b<4 or b>9:
            raise ValueError("Your number is outside of the scope.")
        
    
except ValueError as e :
    
    print(e, "or in simple word you have to enter int value")
        
