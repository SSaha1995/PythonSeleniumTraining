# Task 2 - Program 2
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.

a = int(input("Enter the a number\n"))
b = int(input("Enter the b number\n"))

if a > b:
    print(a, " is greater than ", b)
elif a < b:
    print(a, " is lesser than ", b)
else:
    print(a, " is equal to ", b)