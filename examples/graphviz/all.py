#!/usr/bin/env python
'''
Execute all pycallgraph examples in this directory.
'''
from glob import glob
import os


curdir = os.path.dirname(os.path.abspath(__file__))
examples = glob(os.path.join(curdir, '*.py'))
examples.remove(os.path.join(curdir,'all.py'))
for example in examples:
    print(example)
    execfile(example)