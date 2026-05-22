# Exercises Documentation

Complete reference guide for all exercises in the AI/ML Engineer Stage 1 course. Each exercise is designed to reinforce specific Python concepts and build foundational programming skills.

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [Week 2 - Lecture 1](#week-2---lecture-1)
- [Week 2 - Lecture 2](#week-2---lecture-2)
- [Running Exercises](#running-exercises)
- [Exercise Guidelines](#exercise-guidelines)

## How to Use This Guide

Each exercise documentation includes:
- **Location**: File path
- **Difficulty**: Exercise complexity level
- **Time**: Estimated completion time
- **Objective**: What you'll learn
- **Concepts**: Key programming concepts
- **Requirements**: Input/output specifications
- **Code Explanation**: Detailed walkthrough
- **Expected Output**: Sample execution results
- **Learning Notes**: Tips and common mistakes
- **Extensions**: Challenge variations

## Week 2 - Lecture 1

This lecture introduces basic Python concepts: variables, data types, and output operations.

### Part C: Variables and Print Statements

**Location**: `week_2/lecture_1/part_c.py`

**Difficulty**: ⭐ Beginner

**Time**: 5 minutes

**Objective**
Learn how to:
- Declare variables and assign values
- Use the print() function
- Output text to the console
- Understand string concatenation

**Concepts Covered**
- Variable assignment and naming conventions
- String data type
- print() function with multiple arguments
- String concatenation operators

**Requirements**

**Input**: None (no user input required)

**Output**: 
```
Hello, I am [name]
I am from [school]
```

**Code Explanation**

```python
fname = "Ravindu"              # Declare string variable fname
schl = "Ananda College"        # Declare string variable schl

# Print statement 1: Multiple arguments separated by commas
print("Hello, I am", fname)    # Prints: Hello, I am Ravindu

# Print statement 2: Multiple arguments separated by commas
print("I am from ", schl)      # Prints: I am from Ananda College
```

**Key Points**:
1. Variable names should be descriptive (fname for first name)
2. String values must be enclosed in quotes (" or ')
3. print() function automatically adds spaces between arguments
4. Multiple arguments to print() are separated by commas

**Expected Output**
```
Hello, I am Ravindu
I am from  Ananda College
```

**Learning Notes**
- Notice the extra space before "Ananda College" due to the space in the string literal
- The print() function is the primary way to display output in Python
- Variable names are case-sensitive (fname ≠ Fname)

**Extensions/Challenges**
1. Modify the names and school to your own information
2. Add more variables (age, city, etc.)
3. Use string concatenation with `+` operator instead of comma separation:
   ```python
   print("Hello, I am " + fname)
   ```
4. Create a more complex output with multiple lines

---

## Week 2 - Lecture 2

This lecture covers data structures (lists), loops, conditional statements, and basic data manipulation.

### Part B: Statistics from Student Marks

**Location**: `week_2/lecture_2/part_b.py`

**Difficulty**: ⭐⭐ Intermediate

**Time**: 15 minutes

**Objective**
Learn how to:
- Create and populate lists
- Use for loops to iterate
- Apply built-in functions (max, min, sum, len)
- Perform calculations on collections
- Display calculated results

**Concepts Covered**
- Lists and list operations
- for loops with range()
- User input with input() function
- Type conversion with int()
- Built-in functions: max(), min(), sum(), len()
- String formatting with .format()
- Mathematical operations (division)

**Requirements**

**Input**: 10 integer values representing student marks

**Output**:
- Maximum marks of students
- Minimum marks of students
- Average marks of students

**Code Explanation**

```python
# Initialize empty list and set number of students
marks = []                              # Empty list to store marks
no_of_students = 10

# Collect marks from users
for i in range(no_of_students):        # Loop from 0 to 9 (10 iterations)
    # Format string with loop counter (add 1 to display 1-10 instead of 0-9)
    marks.append(int(input("Please enter the marks for the student no. {no}: ".format(no=i+1))))

# Calculate and display statistics
print("maximum marks of students is", max(marks))           # Find largest value
print("minimum marks of students is", min(marks))           # Find smallest value
print("average marks of students is", str(sum(marks)/no_of_students))  # Sum divided by count
```

**Key Points**:
1. `marks = []` creates an empty list
2. `append()` adds elements to the end of a list
3. `range(n)` generates numbers from 0 to n-1
4. `input()` reads user input as a string
5. `int()` converts string to integer
6. `.format(no=i+1)` inserts values into the string
7. `max()`, `min()`, `sum()` are built-in functions for lists
8. Average = sum / count

**Expected Output**
```
Please enter the marks for the student no. 1: 75
Please enter the marks for the student no. 2: 82
Please enter the marks for the student no. 3: 90
...
Please enter the marks for the student no. 10: 88
maximum marks of students is 95
minimum marks of students is 68
average marks of students is 82.5
```

**Learning Notes**
- The loop uses `i+1` to display student numbers starting from 1 instead of 0
- The average is calculated using integer division (result may have decimals)
- `str()` converts the numeric result to a string for proper output formatting

**Extensions/Challenges**
1. Add median calculation (middle value when sorted)
2. Count how many students scored above the average
3. Grade the average (A, B, C, etc.)
4. Handle variable number of students (ask user how many)
5. Calculate standard deviation

---

### Part C: Grade Calculation System

**Location**: `week_2/lecture_2/part_c.py`

**Difficulty**: ⭐⭐ Intermediate

**Time**: 15 minutes

**Objective**
Learn how to:
- Create and populate lists
- Use for loops with conditional logic
- Implement if/elif/else statements
- Apply grading rules based on numerical input
- Use enumerate() for indexed iteration
- Format output with .format()

**Concepts Covered**
- Lists
- for loops
- enumerate() function
- if/elif/else statements
- Comparison operators (>=, <)
- Nested conditionals
- String formatting

**Requirements**

**Input**: 5 integer values representing marks for different subjects

**Output**: Grade for each subject based on:
- >= 75: A
- >= 65: B
- >= 55: C
- >= 45: S
- < 45: F

**Code Explanation**

```python
marks = []                                    # Empty list for marks
no_of_subs = 5                               # Number of subjects

# Collect marks for each subject
for i in range(no_of_subs):
    marks.append(int(input("Enter marks for the subject no. {no}: ".format(no=i+1))))

print("")                                     # Print blank line for clarity

# Process marks and assign grades
for sub_no, mark in enumerate(marks, start=1):  # start=1 makes numbering begin at 1
    # Evaluate mark and assign grade
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
```

**Key Points**:
1. `enumerate(marks, start=1)` provides both index and value
2. `if/elif/else` evaluates conditions in order
3. First matching condition's code block executes
4. Conditions use >= (greater than or equal)
5. Multiple conditions can be tested with elif

**Expected Output**
```
Enter marks for the subject no. 1: 85
Enter marks for the subject no. 2: 70
Enter marks for the subject no. 3: 62
Enter marks for the subject no. 4: 50
Enter marks for the subject no. 5: 40

Your grade for subject no. 1 is A
Your grade for subject no. 2 is B
Your grade for subject no. 3 is C
Your grade for subject no. 4 is S
Your grade for subject no. 5 is F
```

**Learning Notes**
- The if/elif/else chain checks conditions from top to bottom
- Once a condition is True, that block executes and others are skipped
- Grade ranges are checked in descending order for efficiency
- enumerate() is useful when you need both index and value

**Extensions/Challenges**
1. Add weighted grades (different weights for different subjects)
2. Calculate GPA (convert letters to points, average them)
3. Display Pass/Fail instead of letter grades
4. Add extra credit bonus options
5. Generate a report with grades for multiple students

---

### Part D: Sum with Terminator

**Location**: `week_2/lecture_2/part_d.py`

**Difficulty**: ⭐⭐ Intermediate

**Time**: 15 minutes

**Objective**
Learn how to:
- Use while loops for indefinite iterations
- Implement break statements for loop termination
- Validate user input against termination conditions
- Build lists dynamically during runtime
- Sum values in a collection

**Concepts Covered**
- while loops
- break statement
- Conditional statements in loops
- List operations
- User input handling
- sum() function
- Infinite loop concepts and termination

**Requirements**

**Input**: 
- Series of integer values (indefinite number)
- User enters -999 to terminate input

**Output**: 
- Sum of all entered numbers (excluding the terminator)

**Code Explanation**

```python
nums = []                                    # Empty list to store numbers
terminator = -999                            # Special value that stops input

# Display instruction to user
print("Please enter {} to terminate the program".format(terminator))

# Indefinite loop - continues until break statement
while True:
    num = int(input("Enter a number: "))
    
    # Check if terminator was entered
    if num == terminator:
        break                                # Exit the while loop
    else:
        nums.append(num)                    # Add number to list

# Display result
print("Sum of the entered numbers is: ", sum(nums))
```

**Key Points**:
1. `while True` creates an infinite loop
2. `break` exits the loop immediately
3. Conditions check specific termination value
4. Numbers are only added if not the terminator
5. `sum()` calculates total after loop completes

**Expected Output**
```
Please enter -999 to terminate the program
Enter a number: 10
Enter a number: 20
Enter a number: 15
Enter a number: 25
Enter a number: -999
Sum of the entered numbers is:  70
```

**Learning Notes**
- While loops are useful when the number of iterations is unknown
- The terminator value (-999) should be outside normal input range
- break immediately exits the loop without running remaining code
- Alternative: Use `while num != terminator:` instead of break
- The terminator is NOT included in the sum

**Extensions/Challenges**
1. Count how many numbers were entered
2. Find average instead of sum
3. Find maximum and minimum entered values
4. Use different terminator value (0 or -1)
5. Validate input (reject negative numbers except terminator)
6. Calculate sum and product
7. Keep running total and display after each input

---

## Running Exercises

### Run Individual Exercise

```bash
# Navigate to project directory
cd AI_ML_Engineer_stage_1

# Run exercise with Poetry
poetry run python week_2/lecture_1/part_c.py
poetry run python week_2/lecture_2/part_b.py
poetry run python week_2/lecture_2/part_c.py
poetry run python week_2/lecture_2/part_d.py
```

### Run Without Poetry (if environment activated)

```bash
python week_2/lecture_1/part_c.py
python week_2/lecture_2/part_b.py
```

### Interactive Testing

Run Python interactive shell:
```bash
poetry shell
python
```

Then import and test:
```python
from week_2.lecture_1 import part_c
# View variables
print(part_c.fname)
print(part_c.schl)
```

## Exercise Guidelines

### Before Starting
- Read the entire exercise documentation
- Understand the objectives and concepts
- Review the expected output
- Ask questions if unclear

### During Exercise
- Type code, don't copy-paste (builds muscle memory)
- Pay attention to syntax (indentation, colons, etc.)
- Test frequently
- Use print() statements to debug
- Read error messages carefully

### After Completing
- Verify output matches expected output
- Test with different inputs
- Review your code and understand each line
- Try the extensions/challenges
- Document any issues encountered

### Common Mistakes
1. **Indentation errors**: Python requires consistent indentation
2. **String vs. Integer**: Remember to convert with int()
3. **Loop range**: range(n) goes from 0 to n-1
4. **List indexing**: Lists start at index 0, not 1
5. **Comparison operators**: == (equal), != (not equal), >= (greater than or equal)

### Performance Tips
- Use descriptive variable names
- Add comments to complex logic
- Test with edge cases (0, negative numbers, etc.)
- Review built-in functions before writing your own

---

## Next Steps

- Complete all exercises in order
- Try the extension challenges
- Move on to the next week when ready
- Review and refactor code for clarity

**Last Updated:** May 22, 2026

**Questions?** Refer to Python documentation or ask your instructor.
