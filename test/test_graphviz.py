import pytest
import os

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from test.calls import one_nop


@pytest.fixture
def graphviz(temp):
    g = GraphvizOutput()
    g.output_file = temp
    g.output_type = 'dot'
    return g


def test_simple(graphviz):
    with PyCallGraph(output=graphviz):
        one_nop()
    dot = open(graphviz.output_file).read()
    os.unlink(graphviz.output_file)

    assert 'digraph G' in dot
    assert 'subgraph cluster_test' in dot
