# Task 2
# Python program to compute sum of digits in number.
# Function to get sum of digits  
def getSum(number):
    add = 0
    while number != 0:
        add = add + (number % 10)
        number = number // 10

    return add


n = int(input("Enter a number to compute sum of digits in number: \n"))
print("Sum of digits of", n, "is :", getSum(n))
