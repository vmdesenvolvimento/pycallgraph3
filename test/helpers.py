# flake8: noqa
import time

import pytest

import fix_path
from pycallgraph2 import *
from pycallgraph2.tracer import *
from pycallgraph2.output import *


def wait_100ms():
    time.sleep(0.1)


def wait_200ms():
    time.sleep(0.2)
