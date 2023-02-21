def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = int(input("enter a integer value to find facorial:"))
print("The factorial of", num, "is", factorial(num))
"""
input:
enter a integer value to find facorial:4
output:
The factorial of 4 is 24
"""
