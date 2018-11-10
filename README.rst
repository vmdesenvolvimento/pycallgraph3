Python Call Graph
#################

Note: This is a fork of the original `pycallgraph <https://github.com/gak/pycallgraph>` since it became unmaintained.

Welcome! Python Call Graph is a `Python <http://www.python.org>`_ module that creates `call graph <http://en.wikipedia.org/wiki/Call_graph>`_ visualizations for Python applications.

Project Status
==============

The latest version is **1.1.0** which was released on 2018-11-10, and is a backwards incompatible from the previous release.

The `project lives on GitHub <https://github.com/daneads/pycallgraph2>`_, where you can `report issues <https://github.com/daneads/pycallgraph2/issues>`_, contribute to the project by `forking the project <https://help.github.com/articles/fork-a-repo>`_ then creating a `pull request <https://help.github.com/articles/using-pull-requests>`, or just browse the source code.

The documentation needs some work still. Feel free to contribute :)

Features
========

* Support for Python 2.7+ and Python 3.3+.
* Static visualizations of the call graph using various tools such as Graphviz and Gephi.
* Execute pycallgraph from the command line or import it in your code.
* Customisable colors. You can programatically set the colors based on number of calls, time taken, memory usage, etc.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.

Quick Start
===========

Installation is easy as::

    pip install pycallgraph2

The following examples specify graphviz as the outputter, so it's required to be installed. They will generate a file called **pycallgraph.png**.

The command-line method of running pycallgraph is::

    $ pycallgraph2 graphviz -- ./mypythonscript.py

A simple use of the API is::

    from pycallgraph2 import PyCallGraph
    from pycallgraph2.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        code_to_profile()

Documentation
=============

Documentation for the fork is a work in progress.
