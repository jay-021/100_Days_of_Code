import time
import random
# we'll create question_List for storing the questions

QuestionsList = ["What is a tuple in Python?\n", "Which of the following statements is true about lists and tuples in Python?\n",
                "How do you access the first element of a list in Python?\n", "What is the correct syntax for defining a function in Python?\n",
                "What is the correct syntax for creating a for loop in Python?\n",
                "How do you convert a string to an integer in Python?\n",
                "How do you sort a list in Python?\n"]

# Now let's create correct answers list

CorrectAns = ["An immutable data type that can store multiple values", "Lists are mutable and tuples are immutable",
            "By using the index notation and specifying the index of the element you want to access", "def functionName():",
            "for i in range(10):", "Using the int() function", "Using the sorted() function"]

# Now let's create false answer list

WrongAns = ["A mutable data type that can store multiple values", "A data type that can store multiple values and is always sorted in ascending order",
            'data type that can store multiple values and is always sorted in descending order', "Lists are immutable and tuples are mutable",
            "Both lists and tuples are mutable", "Both lists and tuples are immutable", "By using the first() function",
            "By using the get() function", "By using the last() function", "function functionName()", "function functionName():",
            "def functionName:", "for i in range to 10:", "for (i = 0; i < 10; i++):", "for i in (0,10):", "Using the char() function",
            "Using the float() function", "Using the string() function", "Using the sort() function", "Using the order() function",
            "Using the arrange() function"]

# Now let's create one list for price

MoneyWin = [0, 10, 100, 1000, 10000, 100000,
            1000000, 10000000]  # amount is in USD

# WE HAVE 7 QUESTIONS AND 7 RIGHT ANSWERS AND 21 FALSE ANSWERS AND 7 WINNING PRICE


def time_limited(time_limit):
    """A function that adds a time limit to a block of code.

    Args:
        time_limit (int): The time limit in seconds.

    Returns:
        bool: True if the time limit was not exceeded, False if it was.
    """
    start_time = time.time()
    c = ""
    while c == "":
        c = input("\nYou have 1 min to Choose a, b, c, or d: \t\n")
        if time.time() - start_time > time_limit:
            print("Time limit exceeded.")
            return False
            break
    return c


for i in range(0, 7):
    # select answers from lists
    rightAns = CorrectAns[i]
    a = WrongAns[i*3+1]
    b = WrongAns[i*3]
    c = WrongAns[i*3+2]
    # print question and answers
    print("\n", QuestionsList[i])
    print("a = ", a, "\tb = ", b)
    print("c = ", c, "\td = ", rightAns)

    # function call to select answer within one minute 
    YourAns = time_limited(60)

    # if else for win and loose
    if YourAns != "d":
        LooseCall = " Wrong answer You can take {} $. "
        money = LooseCall.format(MoneyWin[i])
        print(money.center(70, "~"))

        break

    elif YourAns == "d":
        WinCall = " Congratulation You won {} $. "
        money = WinCall.format(MoneyWin[i+1])
        print(money.center(70, "~"))
        
end = " Thanks for playing this KBC "
print(end.center(80,"^"))
