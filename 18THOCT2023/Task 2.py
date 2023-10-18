# Task 2
#  program using break to exit a loop when i == 51 while printing the values from 1 to 100

i = 1               # initialize the value with 1
# Start Printing the Value from 1 to 100
while i <= 100:
    print(i, end=' ')
    if i == 51:     # giving a condition to break
        break
    i += 1
