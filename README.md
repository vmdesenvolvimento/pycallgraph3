[![CircleCI](https://circleci.com/gh/daneads/pycallgraph2.svg?style=svg)](https://circleci.com/gh/daneads/pycallgraph2)

# Python Call Graph 3

**Note**: This is a fork of the original lib [pycallgraph](https://github.com/gak/pycallgraph) since it became
unmaintained and was archived, and of the second lib [pycallgraph2](https://github.com/daneads/pycallgraph2 
that doesn't receive updates for a long time. Python Call Graph 3 is a [Python](http://www.python.org) module that
creates [call graph](http://en.wikipedia.org/wiki/Call_graph) visualizations for Python applications. Python
 Call Graph 3 supports Python 3.x only.
  
## Project Status

The main difference between pycallgraph3 to pycallgraph2 is that in pycallgraph3 only supports Python 3.x.

The project lives on [GitHub](https://github.com/vmdesenvolvimento/pycallgraph3), where you can 
[report issues](https://github.com/daneads/pycallgraph2/issues), contribute to the project by 
[forking the project](https://help.github.com/articles/fork-a-repo) then creating a 
[pull request](https://help.github.com/articles/using-pull-requests), or just browse the source code.

The fork documentation is in construction. Feel free to contribute :)

License: [GNU GPLv2](LICENSE)

## Features

* Support for Python 3.x with focus on the latest version.
* Static visualizations of the call graph using various tools such as Graphviz and Gephi.
* Execute pycallgraph from the command line or import it in your code.
* Customisable colors. You can programatically set the colors based on number of calls, time taken, memory usage, 
etc.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.

## Quick Start

OS dependencies:

* Graphviz is open source software and can be installed on Ubuntu/Debian via `apt install graphviz`, or equivalent 
on other distributions. [See here for more information](https://graphviz.org/download/).

Installation is easy as:

    pip install pycallgraph3

The following examples specify graphviz as the outputter, so it's required to be installed. They will generate a 
file called `pycallgraph.png`.

The command-line method of running pycallgraph is::

    $ pycallgraph graphviz -- ./mypythonscript.py

A simple use of the API is::

    from pycallgraph2 import PyCallGraph
    from pycallgraph2.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        code_to_profile()

## Documentation

Documentation for this fork is a work in progress and can be consulted in 
[pycallgraph docs](https://pycallgraph.com.br).
