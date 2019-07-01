#!/usr/bin/env python
"""
This example is trying to make a large graph. You'll need some internet access
for this to work.

"""

from pycallgraph2 import PyCallGraph
from pycallgraph2 import Config
from pycallgraph2.output import GraphvizOutput


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'large.png'
    config = Config(include_stdlib=True)

    with PyCallGraph(output=graphviz, config=config):
        from urllib3 import urlopen
        from xml.dom.minidom import parseString
        parseString(urlopen('http://w3.org/').read())


if __name__ == '__main__':
    main()
