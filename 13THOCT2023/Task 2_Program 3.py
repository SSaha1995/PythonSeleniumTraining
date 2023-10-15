# Task 2 - Program 3
# Use the ternary operator to find the maximum of three numbers entered by the user.
a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))

max_value = (a if a > b and a > c else b if b > a and b > c else c)
print("The max value between three is", max_value)
