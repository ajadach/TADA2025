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


### 2. Install from Requirements File**
```powershell
# Install all required packages from requirements.txt
cd C:\workshop\TADA2025\DemoQADriver
pip install -r requirements.txt
```

### 3. Verify Installation
```powershell
# Test import of DemoQADriver
python -c "from DemoQADriver import DemoQADriver; print('DemoQADriver imported successfully')"

# Test TADA2025 package import
python -c "from TADA2025 import DemoQADriver; print('TADA2025 package imported successfully')"
```


### Available Console Commands
After installation, you can use these commands from anywhere:

```powershell

# Run tests directly with pytest
cd C:\workshop\TADA2025\
python.exe Test_repo\Tests\ test_1.py
```
