# Also called “formatted string literals,”
# f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
# The expressions are evaluated at runtime and then formatted using the __format__ protocol.


# this is old method to format document in python and problem is you need to pass argument in perfect order

letter = "Hello My name is {}, and I am studying in {}"
name = "Jay"
unI = "Vilnius University"

print(letter.format(name, unI))

# New method is use fo f-string
print(f'Hello My name is {name}, and I am studying in {unI}')

# old method to print two decimal after point
txt = "My monthly budget is {bud:.2f} $."
print(txt.format(bud=225.32423))

# same thing using f-string
bud = 225.32423
txt = f"My monthly budget is {bud:.2f} $."
print(txt)

# you can literally print use of f-string using double curly brackets
# double curly braces
print(f"Hello My name is {{name}}, and I am studying in {{unI}}")
