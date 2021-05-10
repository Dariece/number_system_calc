#!/usr/bin/env python
from setuptools import setup

setup(
    name='number-calculator',
    version='0.0.1',
    py_modules=['numberCalculator','number'],
    entry_points={
        'console_scripts': [
            'numberCalculator = numberCalculator:main'
        ]
    }
    , scripts=['numberCalculator.py']
)
