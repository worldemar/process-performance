#!/usr/bin/env python3
"""
    Test for Simple key-value storage based on python dict.
"""

import pytest
from process_performance.dict_storage import Storage

test_keys = [
    {'1': 1}, {2: '2'}, {3: 3}, {'4': '4'}
]

test_values = [
    {'1': 1}, {2: '2'}, {3: 3}, {'4': '4'}
]


@pytest.mark.parametrize("key", test_keys)
@pytest.mark.parametrize("value", test_values)
def test_insert_retrieve(key, value):
    storage = Storage()
    storage[key] = value
    storage.dump()
    assert storage[key] == value


def test_differentiate_dicts_by_values():
    storage = Storage()
    storage[{'x': 1, 'y': 1}] = {'z': 'foo', 't': 'kek'}
    storage[{'x': 2, 'y': 2}] = {'z': 'bar', 't': 'kek'}
    storage.dump()
    assert storage[{'x': 1, 'y': 1}] == {'z': 'foo', 't': 'kek'}
    assert storage[{'x': 2, 'y': 2}] == {'z': 'bar', 't': 'kek'}
