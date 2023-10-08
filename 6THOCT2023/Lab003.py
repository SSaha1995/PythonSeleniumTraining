# Task2:Take a user from input and print a table
n = input('Enter the number to print the table \n')
n = int(n)
print(f'Table of {n} is :')

print(f'{n} X 1  = {n * 1}')
print(f'{n} X 2  = {n * 2}')
print(f'{n} X 3  = {n * 3}')
print(f'{n} X 4  = {n * 4}')
print(f'{n} X 5  = {n * 5}')
print(f'{n} X 6  = {n * 6}')
print(f'{n} X 7  = {n * 7}')
print(f'{n} X 8  = {n * 8}')
print(f'{n} X 9  = {n * 9}')
print(f'{n} X 10 = {n * 10}')

# Use of print with formatting f

# format with f
name = 'Sujan Saha'
age = 28
salary = 100000

print(f'My name is {name} , i am {age} years old and I got salary {salary}.')

# using .format() method
print('my name is {}, I am {} years old and i got salary{}.'.format(name, age, salary))

# format with % operator
print('My name is %s, Iam %d years old and I got salary %g' % (name, age, salary))

# Task3:list of all functions for the string data types
s = 'Sujan is a Great Learning Enthusiast'
print(len(s))
print(type(s))

# Testing strings:
print('1.', s.isalnum())  # Checks if all characters in the string are alphanumeric.
print('2.', s.isalpha())  # Checks if all characters in the string are alphabetic.
print('3.', s.isascii())  # Returns True if all characters in the string are ascii characters
print('4.', s.isdecimal())  # Returns True if all characters in the string are decimals
print('5.', s.isdigit())  # Checks if all characters in the string are digits.
print('6.', s.isidentifier())  # Returns True if the string is an identifier
print('7.', s.islower())  # Returns True if all characters in the string are lower case
print('8.', s.isnumeric())  # Returns True if all characters in the string are numeric
print('9.', s.isprintable())  # Returns True if all characters in the string are printable
print('10.', s.isspace())  # Returns True if all characters in the string are whitespaces
print('11.', s.istitle())  # Returns True if the string follows the rules of a title
print('12.', s.isupper())  # Returns True if all characters in the string are upper case

# Searching for substrings:

print('13.', s.endswith("Enthusiast"))  # Returns “True” if a string ends with the given suffix
print('14.', s.startswith("Sujan"))  # Checks if the string starts with a specified prefix.
print('15.', s.startswith("babu"))  # Checks if the string Starts with a specified suffix.
# str.find(substring)            #Searches for a substring and returns the index of its first occurrence (or -1 if not found).
print('16.', s.find("bad"))  # -1 (if not fount string)
print('17.', s.find("Great"))  # returns 10 (Searches the string for a specified value and returns the last position of where it was found)
print('18.', s.count("a"))  # Returns the number of occurrences of a substring or a character in the string.
print('19.', s.strip())  # Removes leading and trailing whitespace characters.
print('20.',s.split())  # Splits a string into a list of substrings based on whitespace by default (can specify a separator).

# Converting strings:

print('21.', s.capitalize())  # Capitalizes the first character of the string.
print('22.', s.title())  # Capitalizes the first character of each word in the string.
print('23.', s.lower())  # Converts all characters in a string to lowercase.
print('24.', s.upper())  # Converts all characters in a string to uppercase.
print('25.', s.swapcase())  # Swaps the case of characters (Example:uppercase to lowercase and vice versa).
# print(s.replace("old","new")) #Replaces occurrences of a substring with another substring.
print('26.', s.replace("Great", "Phenomenal"))

# str(int_value)
# example
a = 20000
print('27.', type(a))
string = str(a)
print('28.', type(string))
# str(float_value)
b = 34.8347
print('29.', type(b))
string1 = str(b)
print('30.', type(string1))

# string formatting
name = "Sujan"
age = 28
# f-strings
print('31.', f'My name is {name} and I am {age} years old')
# str.format
print('32.', 'My name is {} and I am {} years old.'.format(name, age))
