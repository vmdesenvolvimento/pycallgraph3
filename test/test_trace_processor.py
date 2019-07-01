import re
import sys
import pytest

from test import calls
from pycallgraph2 import Config
from pycallgraph2.tracer import TraceProcessor


@pytest.fixture
def trace_processor(config):
    return TraceProcessor([], config)


def test_empty(trace_processor):
    sys.settrace(trace_processor.process)
    sys.settrace(None)

    assert trace_processor.call_dict == {}


def test_nop(trace_processor):
    sys.settrace(trace_processor.process)
    calls.nop()
    sys.settrace(None)

    assert 'test.calls.nop' in str(trace_processor.call_dict)


def test_one_nop(trace_processor):
    sys.settrace(trace_processor.process)
    calls.one_nop()
    sys.settrace(None)

    assert 'test.calls.one_nop' in str(trace_processor.call_dict)
    assert 'test.calls.nop' in str(trace_processor.call_dict)


def stdlib_trace(trace_processor, include_stdlib):
    trace_processor.config = Config(include_stdlib=include_stdlib)
    sys.settrace(trace_processor.process)
    re.match("asdf", "asdf")
    calls.one_nop()
    sys.settrace(None)
    return trace_processor.call_dict
