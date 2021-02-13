#!/usr/bin/env python3
"""
    Tests for Parameters class
"""

import pytest
from parameter import Parameter
from parameters import Parameters

test_data = [
    (
        [
            Parameter(name="p1", values=[1, 2, 3]),
            Parameter(name="p2", values=["a", "b"]),
            Parameter(name="p3", values=["normal"]),
        ],
        [
            ({'p1': 1}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'b'}, {'p3': 'normal'})
        ],
        [
            ({'p1': 1}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 2}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 2}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'b'}, {'p3': 'normal'})
        ],
        [
            ({'p1': 1}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 1}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 2}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 2}, {'p2': 'b'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'a'}, {'p3': 'normal'}),
            ({'p1': 3}, {'p2': 'b'}, {'p3': 'normal'})
        ]
    )
]


@pytest.mark.parametrize("params,corners,cube,fill", test_data)
def test_generators(params, corners, cube, fill):
    """test_generators"""
    param_space = Parameters(params)
    assert list(param_space.gen_corners()) == corners
    assert list(param_space.gen_cube()) == cube
    assert list(param_space.gen_fill()) == fill
