from pycallgraph3 import Config
from pycallgraph3.output import Output


def test_set_config():
    """Should not raise!"""
    Output().set_config(Config())
