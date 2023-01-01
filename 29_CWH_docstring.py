# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# you can use docstirngs using doc attribute

def starpatt(n):
    '''
    starpatt take input in int and print starpattern accordingly
    '''
    k = 1
    for i in range(0, n):
        for j in range(0, n-k):
            print(" ", end="")
        for j in range(0, k):
            print('*', end=" ")

        k += 1
        print("\n")

n = int(input("Enter the line number: "))
starpatt(n)

# using .__doc__ you can access docstring
print(starpatt.__doc__)
