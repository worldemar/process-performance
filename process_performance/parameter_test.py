#!/usr/bin/env python3
"""
    Tests for Parameter class
"""

import pytest
from process_performance.parameter import Parameter

test_data = [
    (
        "p1",
        [1],
        [{"p1": 1}],
        [{"p1": 1}],
        [{"p1": 1}]
    ),
    (
        "p1",
        [1, 2],
        [{"p1": 1}, {"p1": 2}],
        [{"p1": 1}, {"p1": 2}],
        [{"p1": 1}, {"p1": 2}]
    ),
    (
        "p1",
        [1, 2, 3, 4],
        [{"p1": 1}, {"p1": 4}],
        [{"p1": 1}, {"p1": 2}, {"p1": 3}, {"p1": 4}],
        [{"p1": 1}, {"p1": 4}, {"p1": 2}, {"p1": 3}]
    )
]


@pytest.mark.parametrize("name,values,edges,line,collapse", test_data)
def test_generators(name, values, edges, line, collapse):
    """test_generators"""
    param = Parameter(name=name, values=values)
    assert list(param.gen_edges()) == edges
    assert list(param.gen_line()) == line
    assert list(param.gen_collapse()) == collapse


def test_nonstring_name():
    """test_nonstring_name"""
    with pytest.raises(Parameter.NonStringNameException):
        Parameter(name=1, values=[1])


def test_no_values():
    """test_no_values"""
    with pytest.raises(Parameter.NoValuesException):
        Parameter(name="p1", values=[])
