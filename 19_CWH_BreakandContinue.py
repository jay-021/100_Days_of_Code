# break use for breaking loops
for i in range(11):
    print(10, "*", i, "=", 10*i)
    if (i == 6):
        break
    else:
        print("I love you", end=" ")

print("I leaft the loop at 6. and the next topic is continue")


# continue use for skipping the itreation in loops
for i in range(11):
    print(10, "*", i, "=", 10*i)
    if (i == 6):
        continue
    else:
        print("I love you", end=" ")

print("I skip the loop at 6.")
