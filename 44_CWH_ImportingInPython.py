""" Importing in Python is the process of loading code from a Python module into the current script. 
This allows you to use the functions and variables defined in the module in your current script,
as well as any additional modules that the imported module may depend on. """
import math 
result = math.sqrt(25)
print(result)

# You can also import multiple functions or variables at once by separating them with a comma:
from math import sqrt,pi
result = sqrt(36)
print(result)

""" It's also possible to import all functions and variables from a module using the * wildcard. 
However, this is generally not recommended as it can lead to confusion and make it harder to
understand where specific functions and variables are coming from. 
from math import * 
"""

""" Python also allows you to rename imported modules using the as keyword. This can be useful 
if you want to use a shorter or more descriptive name for a module, or if you want to avoid
naming conflicts with other modules or variables in your code. """
import math as m
print(m.sqrt(49))



""" Python has a built-in function called dir that you can use to view the names of all the functions 
and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module. """
import math
print("This all variables and functions.")
index = 1
for variables in dir(math):
    print(f"{index} : {variables}")
    index += 1