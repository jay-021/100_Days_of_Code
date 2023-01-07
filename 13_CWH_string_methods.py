# strings are immutable
str1 = "HelLo WOrld"
print(len(str1))
print(str1.upper())
print(str1.lower())

# rstrip() method remove external characters from your string
str1 = " Doremon ***** **"
print(str1.rstrip("*"))
str1 = " *** Doremon *******"
print(str1.rstrip("*"))

# split() method split  your string into lists

print(str1.replace("Doremon", "Nobita"))
print(str1.split(" "))

# capitalize() your string perfectly
heading = " introduction to Python "
print(heading.capitalize())

# center() method align the string to the center as sper the parameters given by the user
print(len(heading))
print(heading.center(70, "*"))
print(len(heading.center(70)))

# count() method count return the number of times the given value has occurred withing the given string.
print(heading.count("o"))  # o is 4 time in heading.

# endswith() method checks if the string ends with a given value in true false.
print(heading.endswith("thon "), " \t endswith()\t", heading)

# we can even check for the value in-between the string by providing start and end index position.
print(heading.endswith("oduc", 5, 9), " \t endswith()\t ",
      heading[5:9])  # now it's check slicing part

# startswith() method checks if the string starts with a given value
print(heading.startswith(" intro"), "\t startswith()\t", heading)

# we can do same thing like in endswith
print(heading.startswith("oduc", 5), '\t startswith()\t ', heading[5:9])


# find () method searches for the first occurrence of the given value and return the index where it is present.
# if value is absent then it returns -1
print(heading.find("oduc"))  # we already knew that it starts from 5

# index() it's same as the find but if value is absent from the string then raise an exception error
print(heading.index("oduc"))

# isalnum() is check your string is alpha numeric or not
heading = "IntroductionToPython"
print(heading.isalnum(), " \t isalnum()\t", heading)

# isalpha() checks your string is only made with alphabetic
heading = "IntroductionToPython99"
print(heading.isalpha(), " \t isalpha()\t", heading)

# islower() checks for lower case
print(heading.islower(), " \t islower()\t", heading)

# isupper() checks for upper case
print(heading.isupper(), " \t isupper() \t", heading)

# isprintable()  checks all the values are printable
# it means if you added any kind of escape sequence character  like this \n \t  result will be false
heading = "Introduction\t To python"
print(heading.isprintable(), " \t isprintable()\t", heading)

# isspace() returns true only and only if the string contains white space, else return false
heading = "     "  # space using spacbar
print(heading.isspace(), " \t isspace() \t using spacebar")
heading = "     "  # space using tab
print(heading.isspace(), " \t isspace() \t using tab")

# istitle() return true only if your title is capitalized
heading = "Introduction to Python"
print(heading.istitle(), "\tistitle()\t", heading)

# swapcase() turns uppercase into lower and lower into upper.
print(heading.swapcase(), "\tswapcase()\t", heading)

# title() converts every first words of strings into capital
print(heading.title(), "\ttitle()\t", heading)
