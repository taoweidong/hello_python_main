#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = []

test_requirements = []

setup(
    author="taoweidong",
    author_email='taowd@outlook.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='src',
    name='src',
    packages=find_packages(include=['src', 'src.*']),
    test_suite='test',
    tests_require=test_requirements,
    url='https://github.com/taowd@outlook.com/hello_python_main',
    version='0.1.0',
    zip_safe=False,
)
