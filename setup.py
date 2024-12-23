from setuptools import setup, find_packages

setup(
    name='unit_tests_kr1sscross',
    version='0.1.0',
    description='An application for managing student attendance',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Krystian Krawczyk',
    author_email='krystian.krawczyk@int.pl',
    packages=find_packages(),
    install_requires=[
        #For future dependencies
    ],
    entry_points={
        'console_scripts': [
            'unit-tests=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',