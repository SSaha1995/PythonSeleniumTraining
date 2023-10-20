# Task 1
# Python program to Create a function that checks if a given string is a palindrome
# function to check given string is palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    print(len(str))
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:  # Comparing the start index value with the last index value i.e.
            # str[0]= str[5-0-1] in case of string length is 5
            return False
    return True


# main function
s = str(input("Enter a String to check if it is Palindrome or not: \n"))
ans = isPalindrome(s)  # calling the isPalindrome(s) function which is defined above

# Check if function is returning true or false, based on print the final result
if ans:
    print(s, "is a Palindrome String")
else:
    print(s, "is not a Palindrome String")
