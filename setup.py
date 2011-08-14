#!/usr/bin/env python3

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

VERSION = '0.6.1'
DESCRIPTION = "Python wrapper for extended filesystem attributes"
LONG_DESCRIPTION = """
Extended attributes extend the basic attributes of files and directories
in the file system.  They are stored as name:data pairs associated with
file system objects (files, directories, symlinks, etc).

Extended attributes are currently only available on Darwin 8.0+ (Mac OS X 10.4)
and Linux 2.6+. Experimental support is included for Solaris and FreeBSD.
"""

CLASSIFIERS = [_f for _f in list(map(str.strip,
"""                 
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Operating System :: POSIX :: Linux
Operating System :: POSIX :: BSD :: FreeBSD
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())) if _f]

setup(
    name="xattr",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Bob Ippolito",
    author_email="bob@redivi.com",
    url="http://undefined.org/python/#xattr",
    license="MIT License",
    packages=['xattr'],
    platforms=['MacOS X', 'Linux', 'FreeBSD'],
    ext_modules=[
        Extension("xattr._xattr", ["xattr/_xattr.c"]),
    ],
    entry_points={
        'console_scripts': [
            "xattr = xattr.tool:main",
        ],
    },
    test_suite="xattr.tests.all_tests_suite",
    zip_safe=False,
)
