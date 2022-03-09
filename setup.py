#!/usr/bin/env python

from setuptools import setup, find_packages
from dotenv import load_dotenv
import os
from setup_parser import parse_test_arg

env_file = ".env" # standard location for environment variables
test_env_file = "tests/.env" # location for test environment variables

load_dotenv(test_env_file if parse_test_arg() else env_file) # loads environment variables from the correct environment file

setup(
    name=os.getenv("PACKAGE_NAME"),
    version=os.getenv("VERSION"), # avoids having to change the version in multiple spots (if applicable)
    packages=find_packages(), # without this, subpackages will not be found
    install_requires=[
        # sample dependencies
        "pandas==1.3.4",
        "sklearn==0.0",
        "matplotlib==3.5.0",
        "numpy==1.21.4"
    ],
)
