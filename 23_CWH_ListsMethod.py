colors = ["white", "black", "green", "red", "blue", "yellow"]
print(type(colors))

print("length of colors is ", len(colors))
print(colors)

# we can add values after creating the list using append method
colors.append("pink")
print("append('pink')\t", colors)

colors.remove("white")  # to remove specific value
print("remove('white')\t", colors)

colors.sort()  # to sort list in ascending order
print("sort()\t", colors)

colors.sort(reverse=True)  # reverse=True sort in descending order
print("sort()\t", colors)

colors.reverse()  # reverse list
print("reverse()\t", colors)

# This method returns the index of the first occurrence of the list item.
print("index()\t", colors.index("blue"))
colors.append("pink")
print("count('pink')\t", colors.count("pink"))

print(colors)  # here we have two pink 1st at 3 and second at 5
col = colors  # NOTE it'll not create second list but it just make reference of original
# so if you remove something from second list it's also remove from original list
col.pop(3)
print(colors)  # pink at 3rd index removed in original colors

# instead of making reference you should use copy method which create new list
col = colors.copy()
col.pop(3)  # pop method remove red from third index but in col not from original
print("col = ", col)
print("colors = ", colors)

col.clear()  # as we know clear will clear the list
col.insert(0, "violate")  # insert add value at specific index
col.append("I am not color")
print(col)
newColor = col + colors  # concatenation of 2 list
colors.extend(col)  # it'll add second col into colors
# NOTE it'll change original list if you don't want to change original then create new and concatenate both list inside it
print(newColor)
