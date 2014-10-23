#!/usr/bin/env python

import os
import sys

"""Uncomment the next lines to automate setuptools downloading in case it
does not already exist in the system.
"""
# try:
#     from ez_setup import use_setuptools
# except ImportError:
#     print "ImportError: missing file ez_setup.py"
#     sys.exit(1)
#
# use_setuptools()

try:
    from setuptools import setup, find_packages
except ImportError:
    print "ImportError: template needs setuptools in order to build"
    sys.exit(1)

from template import __version__, __author__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="proj_name",
    version=__version__,
    url="www.template_url.com/template",
    license='mit',
    description="A template project in python",

    author=__author__,
    author_email="chgrivas7@gmail.com",

    long_description=read("README.md"),

    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python"
    ],

    packages=find_packages(),

    install_requires=[
        ''
    ],

    include_package_data=True,
    zip_safe=False
)
