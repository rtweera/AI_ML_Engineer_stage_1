# Contributing Guidelines

Thank you for your interest in contributing to the AI/ML Engineer Stage 1 project! This document provides guidelines for contributing to the repository.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style Guidelines](#code-style-guidelines)
- [Adding New Exercises](#adding-new-exercises)
- [Committing Changes](#committing-changes)
- [Pull Request Process](#pull-request-process)
- [Documentation Standards](#documentation-standards)
- [Testing](#testing)

## Code of Conduct

All contributors are expected to:
- Be respectful and professional
- Welcome feedback and suggestions
- Focus on what is best for the community
- Show empathy towards other contributors
- Report inappropriate behavior to project maintainers

## Getting Started

### Fork the Repository
1. Click "Fork" on the GitHub repository page
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI_ML_Engineer_stage_1.git
   cd AI_ML_Engineer_stage_1
   ```

### Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/short-description` - New feature
- `fix/short-description` - Bug fix
- `docs/short-description` - Documentation
- `exercise/week-lecture-part` - New exercise

### Set Up Development Environment
```bash
poetry install
poetry shell
```

## Development Workflow

### 1. Make Your Changes
- Work on your feature branch
- Make logical, atomic commits
- Test your changes frequently

### 2. Keep Your Branch Updated
```bash
git fetch origin
git rebase origin/main
```

### 3. Run Tests (if applicable)
```bash
poetry run python -m pytest
```

### 4. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

## Code Style Guidelines

### Python Style

Follow **PEP 8** conventions:

#### Naming Conventions
```python
# ✓ Good
student_marks = []
calculate_average()
MAX_MARKS = 100

# ✗ Avoid
studentMarks = []
CalcAvg()
max_marks = 100  # for constants, use UPPER_CASE
```

#### Line Length
- Keep lines under 79 characters
- Break long lines logically

#### Indentation
- Use 4 spaces (not tabs)
- Consistent indentation throughout

#### Comments and Docstrings
```python
# Good comment - explains why, not what
# Calculate average after filtering out outliers
average = sum(filtered_marks) / len(filtered_marks)

# Function docstring
def calculate_grade(marks):
    """
    Calculate letter grade from numerical marks.
    
    Args:
        marks (int): Numerical mark value
    
    Returns:
        str: Letter grade (A, B, C, S, F)
    """
    if marks >= 75:
        return "A"
    # ... rest of implementation
```

#### Spacing
```python
# ✓ Good
x = 1 + 2
if mark >= 75:
    grade = "A"

# ✗ Avoid
x=1+2
if mark>=75:grade="A"
```

### File Organization

```python
# 1. Module docstring
"""
Module: Grade Calculator
Provides functionality for calculating letter grades from marks.
"""

# 2. Imports
import numpy as np
from week_2.lecture_1 import part_c

# 3. Constants
MAX_MARKS = 100
MIN_MARKS = 0

# 4. Functions
def calculate_grade(marks):
    """Calculate and return grade."""
    pass

# 5. Main execution
if __name__ == "__main__":
    # Main code here
    pass
```

### Error Handling
```python
# ✓ Good
try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
except ValueError:
    print("Please enter a valid integer")

# ✗ Avoid
marks = int(input("Enter marks: "))  # Could crash
```

## Adding New Exercises

### Step 1: Create Directory Structure
```bash
mkdir -p week_N/lecture_M
touch week_N/lecture_M/part_X.py
```

### Step 2: Write the Exercise
```python
"""
Exercise: [Title]
Objective: [What students will learn]
Concepts: [Key programming concepts]
"""

# Your exercise code here
```

### Step 3: Test the Exercise
- Run it with different inputs
- Verify expected output
- Test edge cases

### Step 4: Document the Exercise
1. Update `EXERCISES.md` with:
   - Exercise title and location
   - Difficulty level
   - Estimated time
   - Objective and concepts
   - Expected input/output
   - Code explanation
   - Extensions/challenges

2. Update `STRUCTURE.md` if adding new weeks/lectures

3. Update `README.md` learning path if needed

### Example Exercise Template
```python
"""
Week N, Lecture M, Part X: [Exercise Title]

Learning Objectives:
- [Objective 1]
- [Objective 2]
- [Objective 3]

Concepts Covered:
- [Concept 1]
- [Concept 2]

Input:
[Description of input]

Expected Output:
[Sample output]
"""

# Exercise implementation
def main():
    """Main function for exercise."""
    # Code here
    pass

if __name__ == "__main__":
    main()
```

## Committing Changes

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

**Type**: 
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `exercise`: New exercise
- `test`: Tests

**Subject**: 
- Use imperative mood ("add" not "added")
- Don't capitalize first letter
- No period at end
- Max 50 characters

**Body** (optional):
- Explain what and why, not how
- Max 72 characters per line
- Separate from subject with blank line

**Footer** (optional):
- Reference issues: `Closes #123`
- Breaking changes: `BREAKING CHANGE: description`

### Example Commits
```bash
# Simple fix
git commit -m "fix: correct grade calculation logic"

# Feature with description
git commit -m "feat: add extended student data analysis

- Calculate quartiles
- Generate histogram
- Export to CSV"

# Exercise addition
git commit -m "exercise: add Week 2 Lecture 3 exercises

Add part_a.py with advanced list operations
Add part_b.py with dictionary implementations
Update EXERCISES.md with descriptions"
```

### Commit Checklist
- [ ] Changes are on appropriate branch
- [ ] Code follows style guidelines
- [ ] Tests pass (if applicable)
- [ ] Commit message is clear and descriptive
- [ ] Documentation is updated
- [ ] No sensitive data included

## Pull Request Process

### Before Creating PR
1. Ensure your branch is up to date:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. Push your changes:
   ```bash
   git push origin feature/your-feature-name
   ```

### Create Pull Request
1. Go to the repository on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Exercise addition

## Related Issues
Closes #123

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
Describe how the changes were tested

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Commits are clean and descriptive
- [ ] No breaking changes (or clearly noted)
```

### PR Review Process
- Wait for at least one review
- Address feedback constructively
- Update PR with requested changes
- Request re-review after updates

## Documentation Standards

### README/Guide Format
- Use clear, descriptive headings
- Include table of contents for longer documents
- Use code blocks with language specification
- Include examples where helpful
- Keep language simple and clear

### Exercise Documentation
- Start with clear objectives
- Explain concepts before code
- Include complete code examples
- Show expected output
- Add extensions for advanced learners
- Provide learning notes and common mistakes

### Comments in Code
```python
# ✓ Good comments
# Check if mark qualifies for grade A (>= 75)
if mark >= 75:
    grade = "A"

# ✗ Poor comments
# This is an if statement
if mark >= 75:  # if mark is 75 or more
    grade = "A"  # grade becomes A
```

## Testing

### Test Your Exercise
1. Run with various inputs
2. Test boundary conditions
3. Check for error handling
4. Verify output format

### Example Testing
```bash
# Run exercise directly
python week_2/lecture_1/part_c.py

# Test with Poetry
poetry run python week_2/lecture_2/part_b.py

# Interactive testing
poetry shell
python
>>> from week_2.lecture_1 import part_c
>>> print(part_c.fname)
```

## Common Contribution Scenarios

### Fixing a Typo
1. Create branch: `git checkout -b fix/typo-in-readme`
2. Make change
3. Commit: `git commit -m "fix: correct typo in README"`
4. Push and create PR

### Adding New Exercise
1. Create branch: `git checkout -b exercise/week-2-lecture-3`
2. Create exercise files
3. Test thoroughly
4. Update documentation
5. Commit with clear message
6. Create PR with description

### Improving Documentation
1. Create branch: `git checkout -b docs/improve-setup-guide`
2. Update documentation files
3. Verify formatting
4. Commit: `git commit -m "docs: clarify Poetry installation steps"`
5. Create PR

## Getting Help

- Check existing documentation
- Search closed issues for solutions
- Ask questions in pull request discussions
- Contact project maintainers

## Recognition

Contributors will be recognized in:
- Commit history
- Pull request discussions
- Project documentation (for significant contributions)

Thank you for contributing! 🎉

---

**Last Updated:** May 22, 2026
