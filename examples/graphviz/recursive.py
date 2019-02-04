#!/usr/bin/env python
'''
This example demonstrates a simple recursive call.
'''
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'recursive.png'

    with PyCallGraph(output=graphviz):
        for a in xrange(1, 10):
            factorial(a)

if __name__ == '__main__':
    main()
