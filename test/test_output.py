from pycallgraph2 import Config
from pycallgraph2.output import Output


def test_set_config():
    """Should not raise!"""
    Output().set_config(Config())
