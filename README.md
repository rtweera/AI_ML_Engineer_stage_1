# AI/ML Engineer Stage 1 - Learning Repository

A comprehensive Python learning repository for students beginning their AI and ML engineering journey. This repository contains practical exercises and code examples for fundamental Python programming concepts.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Quick Start](#quick-start)
- [Learning Path](#learning-path)
- [Exercises](#exercises)
- [Contributing](#contributing)
- [Resources](#resources)

## Overview

This repository is designed to build foundational Python programming skills required for AI/ML engineering. It includes practical exercises covering:

- Basic Python syntax and operations
- Data structures (lists, dictionaries, etc.)
- Control flow (loops, conditionals)
- Functions and modular programming
- File I/O and data manipulation
- Basic numerical computations with NumPy

## Prerequisites

- **Python 3.8 or higher** (compatible with Python 3.8.x)
- **pip** package manager
- **Git** for version control
- Basic familiarity with command-line terminal

## Project Structure

```
AI_ML_Engineer_stage_1/
├── README.md                 # This file - Project overview
├── STRUCTURE.md              # Detailed directory structure
├── SETUP_GUIDE.md            # Installation and environment setup
├── EXERCISES.md              # Detailed exercise descriptions
├── CONTRIBUTING.md           # Contribution guidelines
├── DEPENDENCIES.md           # External dependencies documentation
├── main.py                   # Main entry point
├── pyproject.toml            # Project configuration (Poetry)
├── poetry.lock               # Locked dependency versions
├── Git Commands.txt          # Common git commands reference
└── week_2/
    ├── lecture_1/            # Week 2, Lecture 1 exercises
    │   └── part_c.py
    └── lecture_2/            # Week 2, Lecture 2 exercises
        ├── part_b.py
        ├── part_c.py
        └── part_d.py
```

For a detailed explanation of each component, see [STRUCTURE.md](STRUCTURE.md).

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/rtweera/AI_ML_Engineer_stage_1.git
cd AI_ML_Engineer_stage_1
```

### Step 2: Install Poetry (Python Dependency Manager)

Poetry simplifies dependency management in Python projects.

**On macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**On Windows:**
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Or install via pip:
```bash
pip install poetry
```

### Step 3: Install Dependencies

Navigate to the project directory and run:

```bash
poetry install
```

This will:
- Create a virtual environment
- Install all required dependencies (specified in `pyproject.toml`)
- Lock the versions (recorded in `poetry.lock`)

### Step 4: Activate Virtual Environment

```bash
poetry shell
```

Or use:
```bash
source $(poetry env info --path)/bin/activate  # macOS/Linux
.\$(poetry env info --path)\Scripts\activate   # Windows
```

For more detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md).

## Quick Start

### Run the Main Script

```bash
poetry run python main.py
```

### Run Individual Exercises

```bash
# Week 2, Lecture 1
python week_2/lecture_1/part_c.py

# Week 2, Lecture 2
python week_2/lecture_2/part_b.py
python week_2/lecture_2/part_c.py
python week_2/lecture_2/part_d.py
```

## Learning Path

### Week 2 - Fundamentals

**Lecture 1: Basic Python**
- Variables and data types
- Print statements and basic I/O
- See [Exercises](EXERCISES.md#week-2-lecture-1) for details

**Lecture 2: Data Structures & Control Flow**
- Lists and loops
- Conditional statements
- String formatting
- Input/output operations
- See [Exercises](EXERCISES.md#week-2-lecture-2) for details

## Exercises

Each exercise is designed to reinforce specific Python concepts. For complete descriptions, objectives, and expected outputs, see [EXERCISES.md](EXERCISES.md).

### Quick Reference:
- **Lecture 1**
  - `part_c.py`: Variables and Print Statements

- **Lecture 2**
  - `part_b.py`: Statistics from List of Numbers
  - `part_c.py`: Grade Calculation System
  - `part_d.py`: Sum with User Input

## Contributing

We welcome contributions! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- How to add new exercises
- Commit message conventions
- Pull request process

## Dependencies

The project uses the following key dependencies:

- **NumPy** (^1.22.2): Fundamental package for numerical computing
- **Python** (>=3.8.0, <3.9): Programming language version

For more information, see [DEPENDENCIES.md](DEPENDENCIES.md).

## Useful Commands

### Git Operations
```bash
git status           # Check repository status
git add .            # Stage all changes
git commit -m "msg"  # Commit changes
git pull             # Fetch and merge remote changes
git push             # Push local changes to remote
```

### Poetry Commands
```bash
poetry install       # Install dependencies
poetry add [package] # Add a new dependency
poetry update        # Update dependencies
poetry shell         # Activate virtual environment
poetry run [cmd]     # Run command in virtual environment
```

See [Git Commands.txt](Git%20Commands.txt) for more command examples.

## Additional Resources

- [Python Official Documentation](https://docs.python.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Git Documentation](https://git-scm.com/doc)

## License

This project is provided for educational purposes.

## Contact

For questions or suggestions, please reach out to the course instructors or maintainers.

---

**Last Updated:** May 22, 2026

**Version:** 1.0.0
