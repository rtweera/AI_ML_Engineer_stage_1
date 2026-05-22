"""
Week 2, Lecture 2 - Part D: Sum Numbers Until Terminator

Objective:
    Sum a series of user-input numbers until a special terminator value is entered.

Concepts Covered:
    - while loops and indefinite iteration
    - break statement for loop termination
    - Conditional statements in loops (if/else)
    - User input handling
    - List operations and append()
    - sum() function for calculating totals
    - Infinite loops and termination conditions

Learning Goal:
    Learn how to implement indefinite loops with termination conditions,
    and understand when while loops are appropriate instead of for loops.

Input:
    Series of integers (indefinite number)
    User enters -999 to terminate input

Output:
    Sum of all entered numbers (excluding the terminator value)

Terminator Value:
    -999 (signals end of input, not included in calculation)
"""

# Initialize empty list and define terminator value
nums = []                              # Empty list to store numbers
terminator = -999                      # Special value that stops input

# Display instruction to user
print("Please enter {} to terminate the program".format(terminator))

# Indefinite loop - continues until break statement executes
while True:
    num = int(input("Enter a number: "))
    
    # Check if terminator was entered
    if num == terminator:
        break                          # Exit the while loop immediately
    else:
        nums.append(num)               # Add number to list if not terminator

# Display result - sum of all entered numbers
print("Sum of the entered numbers is: ", sum(nums))