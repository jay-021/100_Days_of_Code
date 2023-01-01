'''
The else block appears after the body of the loop. 
The statements in the else block will be executed after all iterations are completed. 
The program exits the loop only after the else block is executed.

NOTE : SYNTAX

for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block

'''

for i in range(6):
    print("iteration no {}".format(i + 1))
    # if i == 4:
    #     break
    # here if we add break statement it will run out of loop and else both
    # execution of else means loop is not break but loop is over that's why in break it does not run else
else:
    print("Sorry for loop is over")
print("out of for loop")


i = 0
while i < 6:
    print("iteration no {}".format(i + 1))
    i += 1
    if i == 4:
        break
else:
    print("sorry while loop is over")
print("out of while loop")
