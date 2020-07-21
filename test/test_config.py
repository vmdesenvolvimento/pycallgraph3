from pycallgraph3 import Config


def test_init():
    assert Config().groups
    assert Config(groups=False).groups is False
