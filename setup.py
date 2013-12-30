# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import newsletry
version = newsletry.__version__

setup(
    name='newsletry',
    version=version,
    author='',
    author_email='max.theilade@gmail.com',
    packages=[
        'newsletry',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['newsletry/manage.py'],
)