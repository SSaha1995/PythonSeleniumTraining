# Task 1
# Get the numerical grade from the user
number = int(input("Enter your numerical grade: "))

# Calculate the letter grade based on the grading scale
letter_grade = ""
if number >= 90:
    letter_grade = "A"
elif number >= 80:
    letter_grade = "B"
elif number >= 70:
    letter_grade = "C"
elif number >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the letter grade to the user
print("Your letter grade is:", letter_grade)