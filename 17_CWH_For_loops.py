# we use loops for executing task multiple time


girls = ["krishna", "Trisha", "Bhumi", "Roopa"]
for girl in girls:
    print(girl, end=" I Love You\n")
    for i in girl:
        print(i)

# range() we use to do it for given time
for i in range(2):
    print(end="I Love You\n")

# normal range (stop)
for i in range(5):
    print(i, end=" ")

#range(start , stop)

for i in range(5, 8):
    print(i, end=' ')
# for  i in range(20000):
#     print(i)

#range (start, stop , step )
print("\nlet's print even numbers in between 0 to 20")
for i in range(0, 21, 2):
    print(i, end=" ")

print(end="\n")
