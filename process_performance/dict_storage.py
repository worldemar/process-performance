#!/usr/bin/env python3
"""
    Simple key-value storage based on python dict.
    Does not have ANY persistence outside of program run time.
    Mostly useful for dry runs and testing purposes.
"""


class Storage:
    def __init__(self):
        self.dictionary = dict()

    def __setitem__(self, key, value):
        self.dictionary[tuple(sorted(key.items()))] = value

    def __getitem__(self, key):
        return self.dictionary[tuple(sorted(key.items()))]

    def dump(self):
        for key, value in self.dictionary.items():
            print("{key} = {value}".format(key=key, value=value))
