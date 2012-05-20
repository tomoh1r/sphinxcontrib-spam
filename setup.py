# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

short_description = "output spam! spam! spam!"
long_description = u'''This package contains the spam Sphinx extension.

This extension enable you to insert spam.

Following code is sample::

    .. spam::
'''
version = '0.0.5'
classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    ]
install_requires = [
    'distribute',
    'Sphinx>=1.1.3',
    ]
if sys.version_info[0:2] == (2, 6):
    install_requires.append('argparse')

setup(
    name='sphinxcontrib-spam',
    version=version,
    url=r"https://github.com/jptomo/sphinxcontrib-spam",
    license='New BSD',
    author="Tomohiro Nakamura",
    author_email="quickness.net at gmall.com",
    description=short_description,
    long_description=long_description,
    zip_safe=False,
    classifiers=classifiers,
    platforms='any',
    install_requires=install_requires,
    namespace_packages=['sphinxcontrib'],
    packages=find_packages(),
    package_data={},
    extras_require=dict(
        test=[
            'pytest>=2.2',
            'coverage>=3.5',
            ]
        ),
    test_suite='test.suite',
    tests_require=['pytest']
    )
