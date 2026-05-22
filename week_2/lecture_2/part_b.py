"""
Week 2, Lecture 2 - Part B: Statistics from Student Marks

Objective:
    Calculate and display statistics (max, min, average) from a list of marks.

Concepts Covered:
    - Lists and list operations
    - for loops with range()
    - User input with input() function
    - Type conversion with int()
    - Built-in functions: max(), min(), sum(), len()
    - String formatting with .format()
    - Mathematical calculations (division)
    - append() method for adding items to lists

Learning Goal:
    Learn how to collect data from users, store in a list, and perform
    basic statistical calculations on numerical data.

Input:
    10 integer values representing student marks (0-100)

Output:
    - Maximum marks
    - Minimum marks
    - Average marks
"""

# Initialize empty list and set number of students
marks = []                              # Empty list to store marks
no_of_students = 10

# Collect marks from users
for i in range(no_of_students):        # Loop from 0 to 9 (10 iterations)
    # Format string with student number (add 1 to display 1-10 instead of 0-9)
    marks.append(int(input("Please enter the marks for the student no. {no}: ".format(no=i+1))))

# Calculate and display statistics
print("maximum marks of students is", max(marks))           # Find largest value in list
print("minimum marks of students is", min(marks))           # Find smallest value in list
print("average marks of students is", str(sum(marks)/no_of_students))  # Sum divided by count