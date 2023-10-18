# Task 1
# Get the numerical grade from the user
number = int(input("Enter your numerical grade: "))

# Calculate the letter grade based on the grading scale
letter_grade = ""
if 90 <= number <= 100:
    letter_grade = "A"
elif 80 <= number <= 89:
    letter_grade = "B"
elif 70 <= number <= 79:
    letter_grade = "C"
elif 60 <= number <= 69:
    letter_grade = "D"
elif 0 <= number <= 59:
    letter_grade = "F"
else:
    letter_grade = "Not in Scope"
# Display the letter grade to the user
print("Your letter grade is:", letter_grade)
