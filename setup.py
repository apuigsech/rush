#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

NAME = 'rush'
DESCRIPTION = 'Rush is a versatile, time-saving tool for transcribing and transforming content from a wide range of sources.'
URL = 'https://github.com/apuigsech/rush'
EMAIL = 'albert@puigsech.com'
AUTHOR = 'Albert Puigsech'
REQUIRES_PYTHON = '>=3.9.0'
VERSION = None
LICENSE = 'MIT'
REQUIRED = []


here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
        VERSION = about['__version__']

setuptools.setup(
    name=NAME,
    description=DESCRIPTION,
    version="0.1.0",
    author=AUTHOR,
    author_email=EMAIL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['rush=rush:main'],
    },
    data_files=[('etc/rush', ['default.conf'])],
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
)
