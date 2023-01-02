'''Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. 
Exception handling deals with these events to avoid the program or system crashing, 
and without this process, exceptions would disrupt the normal operation of a program.

When these exceptions or errors occur, the Python interpreter stops the current process and 
passes it to the calling process until it is handled. If not handled, the program will crash.'''


'''try….. except blocks are used in python to handle errors and exceptions. 
The code in try block runs when there is no error. 
If the try block catches the error, then the except block is executed.

try:
    #statements which could generate 
    #exception
except:
    #Solution of generated exception'''

try :   
    n = int(input("Enter the number: "))
    a = [1,2,3,4]
    print(a[n])
except ValueError: # try to enter value which is not int
    print("This is a ValueError you have to enter int.")
except IndexError:  # try to enter value which is out of index
    print("This is IndexError You are running out of index ")

print("I am outside of the try except blocks")
print("And this can be important code so i don't want to stop my program")
print("important program done End")

# for more errors you can read on web : https://www.tutorialsteacher.com/python/error-types-in-python