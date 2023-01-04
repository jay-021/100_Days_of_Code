def func1():
    try:
        list1 = [1,2,3,4,5]
        n = int(input("Enter the index number: "))
        print(list1[n])
        return list1[n]
    except:
        print("some error occurred ")
        return "Error"
    else:
        print("Integer Accepted.")
        # we can also use else but the same problem it'll not going to be executed .
    
    finally:
        print(" I am always executed cause I'm final keyword.")
    # print("I can not execute inside the function because I should need to be inside of any block to execute.")

x = func1()
print(x)







""" 
The finally code block is also a part of exception handling. 
When we handle exception using the try and except block, we can include a finally block at the end. 
The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or 
closing database connection or may be ending the program execution with a delightful message. 
"""
""" 
try:
    #statements which could generate 
    #exception
except:
    #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation 
"""