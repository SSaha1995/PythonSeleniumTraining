# Task 2
# Python Program to Check Leap Year

year = int(input("Enter year to be checked:\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")