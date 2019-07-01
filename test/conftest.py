import tempfile
import pytest

from pycallgraph2 import PyCallGraph, Config


@pytest.fixture(scope='module')
def pycg():
    return PyCallGraph()


@pytest.fixture(scope='module')
def config():
    return Config()


@pytest.fixture(scope='module')
def temp():
    return tempfile.mkstemp()[1]
