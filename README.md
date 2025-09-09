# UI Driver for TADA2025 Workshop

Example driver for Page Object Pattern for UI via CRUD operations using Selenium WebDriver and Robot Framework.

## Prerequisites

Before using the DemoQADriver, ensure you have the following installed on your system:

### System Requirements
- **Python 3.8+** (tested with Python 3.12.3)
- **Google Chrome** browser (for Selenium WebDriver)
- **Git** (for cloning the repository)

### Required Python Packages

The following packages need to be installed in your virtual environment:

```bash
# Core testing framework
pytest

# Selenium and Robot Framework libraries
selenium
robotframework-seleniumlibrary
chromedriver-autoinstaller

# Additional utilities (automatically installed as dependencies)
robotframework
```

## Installation Guide

### 1. Clone and Navigate to Project
```powershell
git clone https://github.com/ajadach/TADA2025
cd C:\workshop\TADA2025
```


### 2. Create and Activate Virtual Environment
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (PowerShell)
.\.venv\Scripts\Activate.ps1

# Alternative activation (Command Prompt)
.\.venv\Scripts\activate.bat
```

### 3. Install TADA2025 Package

**Option A: Install as Editable Package (Recommended for Development)**
```powershell
# Install TADA2025 in editable mode with all dependencies
pip install -e .

# Or install with development tools
pip install -e ".[dev]"
```

**Option B: Install from Requirements File**
```powershell
# Install all required packages from requirements.txt
pip install -r requirements.txt
```

### 4. Verify Installation
```powershell
# Test import of DemoQADriver
python -c "from DemoQADriver import DemoQADriver; print('DemoQADriver imported successfully')"

# Test TADA2025 package import
python -c "from TADA2025 import DemoQADriver; print('TADA2025 package imported successfully')"

# Run tests using console command
tada2025-test
```

## Package Installation

### Install from Parent Directory
If you're installing from outside the TADA2025 folder:
```powershell
# Navigate to the parent directory containing TADA2025
cd C:\workshop

# Install TADA2025 as editable package
pip install -e .\TADA2025\

# Or install with development dependencies
pip install -e ".\TADA2025\[dev]"
```

### Available Console Commands
After installation, you can use these commands from anywhere:

```powershell
# Run all tests
tada2025-test

# Alternative: Run tests directly with pytest
pytest C:\path\to\TADA2025\tests\ -v
```

## Project Structure

```
C:\workshop\TADA2025\
├── DemoQADriver/             # Main driver package
│   ├── __init__.py           # Package initialization and exports
│   └── demoqa_driver.py      # Main DemoQADriver implementation
├── TADA2025/                 # Top-level package
│   ├── __init__.py           # Package exports
│   └── scripts.py            # Console scripts
├── tests/                    # Test suite
│   └── test_open_session.py  # Test suite for DemoQADriver
├── .venv/                    # Virtual environment (created after setup)
├── setup.py                  # Package setup (legacy)
├── pyproject.toml            # Modern package configuration
├── requirements.txt          # Dependencies list
├── MANIFEST.in               # Package data inclusion rules
├── LICENSE                   # MIT License
└── README.md                 # This file
```

#### 1. Run All Tests
```powershell
# Run all tests in the test file with verbose output
pytest tests\test_open_session.py -v
```

### Test Output Explanation

- **Integration Tests**: Will open actual Chrome browser windows
- **Unit Tests**: Use mocked selenium, run faster without opening browsers
- **Test Duration**: Integration tests take ~20-25 seconds, unit tests are nearly instantaneous

### Example Test Run Output
```
============== test session starts ==============
platform win32 -- Python 3.12.3, pytest-8.4.2
collected 10 items

tests/test_open_session.py::test_open_browser PASSED     [ 10%]
tests/test_open_session.py::test_open_browser_with_alias PASSED [ 20%]
tests/test_open_session.py::test_open_browser_headless PASSED   [ 30%]
tests/test_open_session.py::test_navigate_to_page PASSED        [ 40%]
tests/test_open_session.py::test_close_browser PASSED           [ 50%]
tests/test_open_session.py::test_open_browser_mock PASSED       [ 60%]
tests/test_open_session.py::test_open_browser_headless_mock PASSED [ 70%]
tests/test_open_session.py::test_navigate_to_page_mock PASSED   [ 80%]
tests/test_open_session.py::test_navigate_to_page_default_url_mock PASSED [ 90%]
tests/test_open_session.py::test_close_browser_mock PASSED      [100%]

============== 10 passed in 21.84s ==============
```

## Usage

### Import Options
After installation, you can import the library in multiple ways:

```python
# Option 1: Import from DemoQADriver package directly
from DemoQADriver import DemoQADriver

# Option 2: Import from TADA2025 package
from TADA2025 import DemoQADriver

# Option 3: Import specific components
from DemoQADriver.demoqa_driver import DemoQADriver, SELENIUM
```
