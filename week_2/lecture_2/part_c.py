"""
Week 2, Lecture 2 - Part C: Grade Calculation System

Objective:
    Convert numerical marks to letter grades based on predefined rules.

Concepts Covered:
    - Lists and list operations
    - for loops with iteration
    - enumerate() function for indexed iteration
    - Conditional statements: if/elif/else
    - Comparison operators: >= (greater than or equal)
    - String formatting with .format()
    - Decision logic based on value ranges

Learning Goal:
    Learn how to implement decision logic using conditionals and apply
    grading rules consistently to multiple values.

Grading Scale:
    >= 75: A
    >= 65: B
    >= 55: C
    >= 45: S
    < 45: F

Input:
    5 integer values representing marks for different subjects (0-100)

Output:
    Grade for each subject based on grading scale above
"""

# Initialize empty list and set number of subjects
marks = []                              # Empty list for subject marks
no_of_subs = 5                         # Number of subjects

# Collect marks for each subject
for i in range(no_of_subs):
    marks.append(int(input("Enter marks for the subject no. {no}: ".format(no=i+1))))

print("")                              # Print blank line for clarity

# Process marks and assign grades
for sub_no, mark in enumerate(marks, start=1):  # start=1 makes numbering begin at 1
    # Evaluate mark and assign corresponding grade
    if mark >= 75:
        grade = "A"
    elif mark >= 65:
        grade = "B"
    elif mark >= 55:
        grade = "C"
    elif mark >= 45:
        grade = "S"
    else:
        grade = "F"
    
    # Display subject number and assigned grade
    print("Your grade for subject no. {sub_no} is {grade}".format(sub_no=sub_no, grade=grade))