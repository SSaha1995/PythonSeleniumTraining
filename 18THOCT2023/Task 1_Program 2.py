# Task 1 - Program 2
# Program to display the Factorial of a given number
num = int(input("Enter a number: "))
factorial = 1

# check if the factorial of number less than 0 is valid
if num < 0:
    print(" Factorial does not exist for negative numbers")

# if there is only one number o, return 1
elif num == 0:
    print("The factorial of 0 is 1")
# generate Factorial of given number
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
