#!/usr/bin/env python

from os import path
from setuptools import setup
import sys

from setuptools.command.test import test as TestCommand

import pycallgraph2

# Only install the man page if the correct directory exists
# XXX: Commented because easy_install doesn't like it
#man_path = '/usr/share/man/man1/'
#if path.exists(man_path):
#    data_files=[['/usr/share/man/man1/', ['man/pycallgraph.1']]]
#else:
#    data_files=None

data_files=None

class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='pycallgraph2',
    version=pycallgraph2.__version__,
    description=pycallgraph2.__doc__.strip().replace('\n', ' '),
    long_description=open('README.rst').read(),
    author=pycallgraph2.__author__,
    license=open('LICENSE').read(),
    url=pycallgraph2.__url__,
    packages=['pycallgraph2', 'pycallgraph2.output'],
    scripts=['scripts/pycallgraph'],
    data_files=data_files,
    use_2to3=True,

    # Testing
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers',
    ],
)
