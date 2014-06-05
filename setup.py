#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import publisher

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = publisher.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='django-model-publisher',
    version=version,
    description="""Handy mixin/abstract class for providing a "publisher workflow" to arbitrary Django models.""",
    long_description=readme,
    author='JP74',
    author_email='tech@jp74.com',
    url='https://github.com/jp74/django-model-publisher',
    packages=[
        'publisher',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-model-publisher',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)