#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
def read_requirements():
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt') as req_file:
            for line in req_file:
                line = line.strip()
                # Skip comments and empty lines
                if line and not line.startswith('#'):
                    # Remove inline comments
                    if '#' in line:
                        line = line.split('#')[0].strip()
                    requirements.append(line)
    return requirements

setup(
    name='TADA2025',
    version='1.0.0',
    author='TADA2025 Workshop',
    author_email='workshop@tada2025.com',
    description='UI Driver library for TADA2025 workshop - Page Object Pattern for UI via CRUD operations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ajadach/TADA2025',
    project_urls={
        'Bug Reports': 'https://github.com/ajadach/TADA2025/issues',
        'Source': 'https://github.com/ajadach/TADA2025',
        'Documentation': 'https://github.com/ajadach/TADA2025/README.me',
    },
    packages=find_packages(exclude=['tests*', '.pytest_cache*', '.venv*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Framework :: Robot Framework',
        'Framework :: Robot Framework :: Library',
    ],
    python_requires='>=3.8',
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest-html>=3.1.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
            'mypy>=0.950',
        ],
        'test': [
            'pytest>=8.0.0',
            'pytest-mock>=3.10.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'tada2025-test=TADA2025.scripts:run_tests',
        ],
    },
    include_package_data=True,
    package_data={
        'TADA2025': ['*.md', '*.txt', '*.rst'],
    },
    zip_safe=False,
    keywords='ui automation testing selenium robot-framework page-object-pattern crud workshop',
)
