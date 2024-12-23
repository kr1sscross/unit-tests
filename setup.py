from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='unit_tests_kr1sscross',
    version='0.1.0',
    description='A sample Python function package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Krystian Krawczyk',
    author_email='krystian.krawczyk@int.pl',
    url='https://github.com/krystian-krawczyk/unit_tests_kr1sscross',  # Update with your repo URL
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