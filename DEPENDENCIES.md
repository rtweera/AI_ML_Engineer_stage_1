# Dependencies Documentation

Reference guide for all project dependencies and their usage in the AI/ML Engineer Stage 1 project.

## Table of Contents

- [Overview](#overview)
- [Production Dependencies](#production-dependencies)
- [Python Version](#python-version)
- [Dependency Management](#dependency-management)
- [Version Information](#version-information)
- [Updating Dependencies](#updating-dependencies)

## Overview

This project uses Poetry for modern Python dependency management. Dependencies are defined in `pyproject.toml` and locked in `poetry.lock` to ensure reproducible builds across different environments.

### Dependency Categories
- **Production Dependencies**: Required to run the project
- **Development Dependencies**: Only needed for development (testing, linting, etc.)

Currently, the project has minimal dependencies focused on core functionality.

## Production Dependencies

### Python
**Requirement**: `>=3.8.0,<3.9`

The project is designed specifically for Python 3.8.x (3.8.0 through 3.8.z, but not 3.9.0+).

**Why Python 3.8?**
- Long-term support release
- Wide availability
- Good balance of features and stability
- Compatible with educational environments

**Versions Tested**:
- Python 3.8.0 through 3.8.13 (latest 3.8)

**Features Used**:
- f-strings (Python 3.6+)
- Type hints (Python 3.5+)
- Positional-only parameters (Python 3.8+)
- Assignment expression walrus operator (Python 3.8+)

**Upgrade Path**:
When upgrading to Python 3.9+, verify:
- Syntax compatibility
- Library compatibility
- Performance implications

---

### NumPy
**Version**: `^1.22.2` (Compatible Release)

**What is NumPy?**
NumPy is a fundamental package for numerical computing in Python. It provides:
- N-dimensional array objects (ndarray)
- Mathematical functions
- Linear algebra operations
- Random number generation
- Fourier transforms
- Broadcasting capabilities

**Version Constraint Explanation**:
- `^1.22.2` means >= 1.22.2, < 2.0.0
- Allows patch and minor version updates
- Prevents major version changes that could break compatibility

**Why NumPy?**
- Essential for data science and machine learning
- Efficient numerical computations
- Foundation for pandas, scikit-learn, etc.
- Fundamental skill for AI/ML engineering

**Installation**:
```bash
poetry install  # Automatically installs NumPy
```

Explicit installation:
```bash
poetry add numpy@^1.22.2
```

**Basic Usage Example**:
```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Mathematical operations
mean = np.mean(arr)
sum_val = np.sum(arr)
sqrt_vals = np.sqrt(arr)

# Random numbers
random_arr = np.random.rand(10)

# Reshaping
reshaped = arr.reshape(5, 1)
```

**NumPy 1.22.2 Features**:
- Improved performance
- Better type safety
- Enhanced compatibility
- Stable API for production use

**Common NumPy Functions in This Course**:

| Function | Purpose |
|----------|---------|
| `np.array()` | Create array from list |
| `np.zeros()` | Create array of zeros |
| `np.ones()` | Create array of ones |
| `np.arange()` | Create sequence of numbers |
| `np.linspace()` | Create evenly spaced numbers |
| `np.mean()` | Calculate average |
| `np.median()` | Calculate median |
| `np.std()` | Calculate standard deviation |
| `np.max()` | Find maximum value |
| `np.min()` | Find minimum value |
| `np.sum()` | Calculate sum |
| `np.dot()` | Matrix multiplication |
| `np.reshape()` | Change array shape |
| `np.transpose()` | Flip array dimensions |

**When to Use NumPy**:
- Working with numerical data
- Mathematical computations
- Image processing
- Matrix operations
- Data manipulation at scale
- Machine learning preprocessing

**Alternative Libraries** (for reference):
- **Pandas**: Higher-level data manipulation (built on NumPy)
- **SciPy**: Scientific computing (extends NumPy)
- **scikit-learn**: Machine learning (uses NumPy)
- **Matplotlib**: Visualization (uses NumPy arrays)

**Learning Resources for NumPy**:
- [NumPy Official Documentation](https://numpy.org/doc/1.22/)
- [NumPy Tutorial](https://numpy.org/doc/1.22/user/absolute_beginners.html)
- [NumPy Cheat Sheet](https://www.datacamp.com/cheat-sheets)

---

## Python Version

### Current Configuration
```toml
[tool.poetry.dependencies]
python = ">=3.8.0,<3.9"
```

### Version Compatibility

**Supported**: Python 3.8.x (any patch version)
- 3.8.0, 3.8.1, 3.8.2, ... 3.8.13 ✓

**Not Supported**: 
- Python 3.7 or earlier ✗
- Python 3.9 or later ✗

### Check Your Python Version

```bash
python --version
python3 --version
python3.8 --version
```

### Managing Multiple Python Versions

If you have multiple Python versions installed:

```bash
# Specify Python version for Poetry
poetry env use /usr/bin/python3.8

# Verify
poetry env info
```

---

## Dependency Management

### Project Configuration File (`pyproject.toml`)

```toml
[tool.poetry]
name = "python-template"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.8.0,<3.9"
numpy = "^1.22.2"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Lock File (`poetry.lock`)

Contains exact versions of all installed packages and transitive dependencies.

**Important**: Always commit `poetry.lock` to version control.

### Virtual Environment

Poetry automatically creates and manages virtual environments.

**Location**:
- Linux/macOS: `~/.cache/pypoetry/virtualenvs/`
- Windows: `%APPDATA%\pypoetry\virtualenvs\`

**Size**: ~500 MB (includes all dependencies)

---

## Version Information

### Current Release Versions

| Package | Version | Release Date |
|---------|---------|--------------|
| Python | 3.8.x | 10/14/2019 |
| NumPy | 1.22.2 | 01/17/2022 |
| Poetry | Latest | Continuous |

### Checking Installed Versions

```bash
# Activate environment
poetry shell

# Check all packages
poetry show

# Check specific package
poetry show numpy

# Check outdated packages
poetry show --outdated

# Check Python version
python --version
```

### NumPy Version History

| Version | Release Date | Status |
|---------|--------------|--------|
| 1.22.2 | 01/17/2022 | Latest for 1.22.x |
| 1.22.0 | 12/31/2021 | Initial 1.22 release |
| 1.21.6 | 01/17/2022 | Older version |
| 2.0.0 | Future | Major version |

---

## Updating Dependencies

### Manual Updates

#### Update All Dependencies
```bash
poetry update
```

#### Update Specific Package
```bash
poetry update numpy
```

#### Add New Dependency
```bash
poetry add numpy@^1.23.0  # Production
poetry add --dev pytest   # Development
```

#### Remove Dependency
```bash
poetry remove numpy
poetry remove --dev pytest
```

### Version Constraint Syntax

| Constraint | Meaning | Example |
|-----------|---------|---------|
| `^` | Compatible Release | `^1.22.2` = `>=1.22.2,<2.0.0` |
| `~` | Approximately Release | `~1.22.2` = `>=1.22.2,<1.23.0` |
| `==` | Exact Version | `==1.22.2` |
| `!=` | Not Version | `!=1.22.2` |
| `>`, `<` | Greater/Less | `>1.22.0` |
| `>=`, `<=` | Greater/Less or Equal | `>=1.22.2` |

### Safe Update Strategy

1. **Understand current versions**:
   ```bash
   poetry show
   ```

2. **Check for updates**:
   ```bash
   poetry show --outdated
   ```

3. **Test before updating**:
   - Record current behavior
   - Test locally with new version
   - Verify all exercises work

4. **Update incrementally**:
   ```bash
   poetry update numpy
   ```

5. **Commit changes**:
   ```bash
   git add poetry.lock
   git commit -m "update: upgrade numpy to latest"
   ```

### Dependency Conflicts

If Poetry reports conflicts:

```bash
# Clear cache and reinstall
poetry install --no-cache

# Force update
poetry update --dry-run  # See what would change
poetry update           # Apply updates
```

---

## Security Considerations

### Vulnerable Dependency Checking

Periodically check for security vulnerabilities:

```bash
# Check Poetry updates
poetry self update

# Review dependency security
# Check: https://pypi.org/project/[package-name]/
```

### Reporting Vulnerabilities

If you find a security issue:
1. Do not publicly disclose
2. Report to project maintainers
3. Allow time for fix before disclosure

### Keeping Dependencies Secure

- Regularly update Poetry: `poetry self update`
- Monitor dependency updates: `poetry show --outdated`
- Test updates in development before production
- Keep Python updated within 3.8.x range

---

## Troubleshooting

### Issue: Poetry Not Finding Python 3.8
**Solution**:
```bash
poetry env use /usr/bin/python3.8
poetry install
```

### Issue: ModuleNotFoundError: No module named 'numpy'
**Solution**:
```bash
poetry install --no-cache
poetry shell
python -c "import numpy; print(numpy.__version__)"
```

### Issue: Dependency Conflict
**Solution**:
```bash
poetry lock --no-update
poetry install
```

### Issue: Virtual Environment Issues
**Solution**:
```bash
poetry env remove 3.8
poetry install
```

---

## Future Dependencies

As the course expands, expected additions:

- **pytest**: Testing framework
- **pandas**: Data analysis (built on NumPy)
- **matplotlib**: Data visualization
- **scikit-learn**: Machine learning
- **jupyter**: Interactive notebooks

---

## Additional Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/1.22/)
- [Python 3.8 Documentation](https://docs.python.org/3.8/)
- [PyPI Package Index](https://pypi.org/)
- [Poetry Dependency Specification](https://python-poetry.org/docs/dependency-specification/)

---

## Summary Table

| Item | Value |
|------|-------|
| Python Version | 3.8.x |
| Python Constraint | `>=3.8.0,<3.9` |
| NumPy Version | 1.22.2+ |
| NumPy Constraint | `^1.22.2` |
| Dependency Manager | Poetry |
| Lock File | poetry.lock |
| Config File | pyproject.toml |

---

**Last Updated:** May 22, 2026

**Current Version**: 1.0.0
