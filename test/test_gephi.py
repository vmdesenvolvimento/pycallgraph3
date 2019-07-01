import pytest
import os

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GephiOutput
from test.calls import one_nop


@pytest.fixture
def gephi(temp):
    g = GephiOutput()
    g.output_file = temp
    return g


def test_simple(gephi):
    with PyCallGraph(output=gephi):
        one_nop()
    generated = open(gephi.output_file).read()
    os.unlink(gephi.output_file)

    assert 'nodedef> name VARCHAR' in generated
    assert 'edgedef> node1 VARCHAR, node2 VARCHAR' in generated
    assert 'test.calls.one_nop,1,true,true' in generated
    assert 'test.calls.one_nop,test.calls.nop,1,true,true' in generated
