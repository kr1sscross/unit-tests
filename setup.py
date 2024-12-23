import os
from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

Version = os.getenv('PACKAGE_VERSION')

setup(
    name='unit_tests_kr1sscross',
    version=Version,
    description='A sample Python function package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Krystian Krawczyk',
    author_email='krystian.krawczyk@int.pl',
    url='https://github.com/kr1sscross/unit-tests',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)