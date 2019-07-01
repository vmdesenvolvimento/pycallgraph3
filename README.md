[![CircleCI](https://circleci.com/gh/daneads/pycallgraph2.svg?style=svg)](https://circleci.com/gh/daneads/pycallgraph2)

# Python Call Graph

Note: This is a fork of the original [pycallgraph](https://github.com/gak/pycallgraph) since it became unmaintained.

Welcome! pycallgraph2 is a [Python](http://www.python.org) module that creates [call graph](http://en.wikipedia.org/wiki/Call_graph) visualizations for Python applications.

## Project Status

The project lives on [GitHub](https://github.com/daneads/pycallgraph2), where you can [report issues](https://github.com/daneads/pycallgraph2/issues), contribute to the project by [forking the project](https://help.github.com/articles/fork-a-repo) then creating a [pull request](https://help.github.com/articles/using-pull-requests), or just browse the source code.

The fork needs documentation. Feel free to contribute :)

License: [GNU GPLv2](LICENSE)

## Features

* Support for Python 2.7+ and Python 3.3+.
* Static visualizations of the call graph using various tools such as Graphviz and Gephi.
* Execute pycallgraph from the command line or import it in your code.
* Customisable colors. You can programatically set the colors based on number of calls, time taken, memory usage, etc.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.

## Quick Start

OS dependencies:

* Graphviz is open source software and can be installed on Ubuntu/Debian via `apt install graphviz`, or equivalent on other distributions.
  [See here for more information](https://graphviz.org/download/).

Installation is easy as:

    pip install pycallgraph2

The following examples specify graphviz as the outputter, so it's required to be installed. They will generate a file called `pycallgraph.png`.

The command-line method of running pycallgraph is::

    $ pycallgraph graphviz -- ./mypythonscript.py

A simple use of the API is::

    from pycallgraph2 import PyCallGraph
    from pycallgraph2.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        code_to_profile()

## Documentation

Documentation for the fork is a work in progress.
