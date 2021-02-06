#!/usr/bin/env python3

import pytest
from parameter import Parameter

def test_generators_1():
    p = Parameter(name="p1", values=[1])
    assert(list(p.line()) == [1])
    assert(list(p.edges()) == [1,1])
    assert(list(p.collapse()) == [1])


def test_generators_2():
    p = Parameter(name="p1", values=[1,2])
    assert(list(p.line()) == [1,2])
    assert(list(p.edges()) == [1,2])
    assert(list(p.collapse()) == [1,2])


def test_generators_4():
    p = Parameter(name="p1", values=[1,2,3,4])
    assert(list(p.line()) == [1,2,3,4])
    assert(list(p.edges()) == [1,4])
    assert(list(p.collapse()) == [1,4,2,3])


def test_nonstring_name():
    with pytest.raises(Parameter.NonStringNameException):
        Parameter(name=1, values=[1])


def test_no_values():
    with pytest.raises(Parameter.NoValuesException):
        Parameter(name="p1", values=[])
