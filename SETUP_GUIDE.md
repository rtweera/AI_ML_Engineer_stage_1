# Setup Guide - Installation & Environment Configuration

A comprehensive guide to setting up your development environment for the AI/ML Engineer Stage 1 project.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Prerequisites Installation](#prerequisites-installation)
3. [Repository Setup](#repository-setup)
4. [Dependency Management with Poetry](#dependency-management-with-poetry)
5. [Verification & Testing](#verification--testing)
6. [Troubleshooting](#troubleshooting)
7. [Working with the Environment](#working-with-the-environment)

## System Requirements

### Minimum Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: 3.8.x or higher (exactly 3.8.x as per project configuration)
- **Disk Space**: ~500 MB (including dependencies)
- **RAM**: 2 GB minimum
- **Internet Connection**: Required for initial setup

### Recommended Setup
- **Python**: 3.8.10 or 3.8.13 (latest 3.8 patch)
- **pip**: 21.0 or higher
- **Git**: 2.30 or higher
- **Terminal**: Bash (Linux/macOS) or PowerShell (Windows)

## Prerequisites Installation

### Step 1: Install Python 3.8

#### On Windows
1. Download Python 3.8 from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH"
4. Choose "Install Now" or customize installation
5. Verify installation:
   ```bash
   python --version
   ```

#### On macOS
Using Homebrew (recommended):
```bash
brew install python@3.8
brew link python@3.8
python3.8 --version
```

Or download from [python.org](https://www.python.org/downloads/):
1. Download macOS installer for Python 3.8
2. Run the installer
3. Verify: `python3.8 --version`

#### On Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3.8 python3.8-venv python3.8-dev
python3.8 --version
```

#### On Linux (Fedora/RHEL/CentOS)
```bash
sudo dnf install python3.8
python3.8 --version
```

### Step 2: Install pip

Pip is Python's package manager. It usually comes with Python 3.8+.

Verify installation:
```bash
pip --version
pip3 --version
```

If not installed:
```bash
python -m ensurepip --upgrade
```

### Step 3: Install Git

#### On Windows
Download from [git-scm.com](https://git-scm.com/download/win) and run the installer.

#### On macOS
```bash
brew install git
```

Or download from [git-scm.com](https://git-scm.com/download/mac)

#### On Linux
```bash
# Ubuntu/Debian
sudo apt-get install git

# Fedora/RHEL/CentOS
sudo dnf install git
```

Verify installation:
```bash
git --version
```

## Repository Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/rtweera/AI_ML_Engineer_stage_1.git
cd AI_ML_Engineer_stage_1
```

Verify you're in the correct directory:
```bash
ls -la  # Should show README.md, main.py, week_2/, etc.
```

### Step 2: Verify Project Files

Ensure all essential files are present:
```bash
ls -la | grep -E "(README|main\.py|pyproject\.toml|poetry\.lock)"
```

Expected output should show:
- `README.md`
- `main.py`
- `pyproject.toml`
- `poetry.lock`

## Dependency Management with Poetry

Poetry is a modern Python dependency management tool that simplifies package installation and virtual environment management.

### Step 1: Install Poetry

#### On Windows, macOS, or Linux
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or using pip:
```bash
pip install poetry
```

Or using Homebrew (macOS):
```bash
brew install poetry
```

Verify installation:
```bash
poetry --version
```

#### Add Poetry to PATH (if needed)
**Windows**: Poetry installer adds to PATH automatically.

**macOS/Linux**: Add to your shell profile (~/.bashrc, ~/.zshrc, ~/.bash_profile):
```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### Step 2: Install Project Dependencies

In the project root directory:

```bash
poetry install
```

This command:
- Reads `pyproject.toml` for project configuration
- Reads `poetry.lock` for exact dependency versions
- Creates a virtual environment (if not exists)
- Installs all dependencies with locked versions
- Ensures reproducibility across machines

Expected output:
```
Creating virtualenv [project-name] in [...]/virtualenvs
Installing dependencies from lock file
  - Installing numpy (1.22.2)
```

### Step 3: Activate the Virtual Environment

#### Option A: Using Poetry Shell
```bash
poetry shell
```

This opens a new shell with the virtual environment activated. You'll see the environment name in your prompt.

#### Option B: Using Direct Activation
Get the environment path:
```bash
poetry env info --path
```

**On Linux/macOS:**
```bash
source $(poetry env info --path)/bin/activate
```

**On Windows (PowerShell):**
```powershell
& $(poetry env info --path)\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
$(poetry env info --path)\Scripts\activate.bat
```

#### Option C: Run Commands Directly
Run commands without activating the environment:
```bash
poetry run python main.py
poetry run python week_2/lecture_1/part_c.py
```

### Step 4: Understanding Poetry Files

#### `pyproject.toml`
Contains project configuration:
```toml
[tool.poetry]
name = "python-template"
version = "0.1.0"
python = ">=3.8.0,<3.9"

[tool.poetry.dependencies]
numpy = "^1.22.2"
```

- **python version**: Defines compatible Python versions
- **dependencies**: Production dependencies
- **dev-dependencies**: Development-only dependencies

#### `poetry.lock`
Auto-generated file containing exact versions of all packages and their dependencies. Always commit this file to ensure reproducibility.

## Verification & Testing

### Step 1: Verify Python Installation

```bash
python --version        # Should show 3.8.x
poetry run python --version
```

### Step 2: Verify Dependencies

```bash
poetry show             # List all installed packages
poetry show numpy       # Show specific package details
```

Expected output should include NumPy 1.22.2 or compatible version.

### Step 3: Test Virtual Environment

```bash
poetry run python -c "import numpy; print(f'NumPy {numpy.__version__}')"
```

Expected output:
```
NumPy 1.22.x
```

### Step 4: Run a Sample Exercise

```bash
poetry run python week_2/lecture_1/part_c.py
```

Expected output:
```
Hello, I am Ravindu
I am from  Ananda College
```

### Step 5: Run Main Script

```bash
poetry run python main.py
```

Should execute without errors.

## Troubleshooting

### Issue: Python 3.8 Not Found
**Solution**: 
- Verify installation: `python3.8 --version`
- Update Poetry: `poetry self update`
- Manually specify Python: `poetry env use /path/to/python3.8`

### Issue: Poetry Command Not Found
**Solutions**:
1. Ensure Poetry is installed: `pip install poetry`
2. Add Poetry to PATH:
   - **macOS/Linux**: Add `export PATH="$HOME/.local/bin:$PATH"` to shell profile
   - **Windows**: Reinstall Poetry with pip

### Issue: ModuleNotFoundError: No module named 'numpy'
**Solutions**:
1. Ensure virtual environment is activated: `poetry shell`
2. Reinstall dependencies: `poetry install --no-cache`
3. Check environment: `poetry env info`

### Issue: Permission Denied (on macOS/Linux)
**Solution**: 
```bash
chmod +x $(poetry env info --path)/bin/python
poetry install --no-cache
```

### Issue: Conflicting Python Versions
**Solution**:
```bash
poetry env remove 3.7  # Remove conflicting versions
poetry install
```

### Issue: Lock File Issues
**Solutions**:
```bash
# Update lock file
poetry update

# Reset lock file to match pyproject.toml
rm poetry.lock
poetry install
```

### Issue: Windows PowerShell Execution Policy
**Solution**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Working with the Environment

### Adding New Dependencies

If you need to add a new package:

```bash
poetry add package_name              # Production dependency
poetry add --dev package_name        # Development dependency
poetry add --dev pytest              # Example: add pytest for testing
```

This automatically updates `pyproject.toml` and `poetry.lock`.

### Updating Dependencies

```bash
poetry update                        # Update all packages
poetry update numpy                  # Update specific package
```

### Viewing Installed Packages

```bash
poetry show                         # List all packages
poetry show --outdated              # Show packages with updates available
```

### Removing Dependencies

```bash
poetry remove package_name          # Remove dependency
poetry remove --dev package_name    # Remove dev dependency
```

### Exiting Virtual Environment

```bash
deactivate              # If using direct activation
exit                    # If using 'poetry shell'
```

## Daily Workflow Commands

### Starting Work Session
```bash
cd AI_ML_Engineer_stage_1
poetry shell
# Now you have access to all project dependencies
```

### Running Exercises
```bash
poetry run python week_2/lecture_1/part_c.py
poetry run python week_2/lecture_2/part_b.py
```

### Committing Changes
```bash
git status
git add .
git commit -m "Complete Week 2 Lecture 1 exercises"
git push
```

### Updating Local Repository
```bash
git pull
poetry install  # Install any new dependencies added by others
```

## Environment Information

Check detailed environment information:

```bash
poetry env info                 # General environment info
poetry env list                 # List all environments
poetry config --list            # Show Poetry configuration
```

## Next Steps

Once setup is complete:

1. Read [README.md](README.md) for project overview
2. Review [STRUCTURE.md](STRUCTURE.md) for directory organization
3. Start with exercises in [EXERCISES.md](EXERCISES.md)
4. Read [CONTRIBUTING.md](CONTRIBUTING.md) if adding new content

## Additional Resources

- [Poetry Official Documentation](https://python-poetry.org/docs/)
- [Python 3.8 Documentation](https://docs.python.org/3.8/)
- [NumPy Documentation](https://numpy.org/doc/1.22/)
- [Git Documentation](https://git-scm.com/doc)

---

**Last Updated:** May 22, 2026

**Need Help?** Check the Troubleshooting section or consult the course instructor.
