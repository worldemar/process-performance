#!/usr/bin/env python3
"""
    One parameter for command line.
    Provides generators to iterate over values.
"""


class Parameter():
    """
    Keeps single parameter name and values.

    Provides generators to iterate over values.
    """

    class NoValuesException(RuntimeError):
        """NoValuesException"""

    class NonStringNameException(RuntimeError):
        """NonStringNameException"""

    def __init__(self, name=None, values=None):
        self.name = name
        self.values = list(values)
        if not isinstance(name, str):
            raise Parameter.NonStringNameException(
                "Parameter name '{name}' is not string".format(name=name))
        if len(self.values) < 1:
            raise Parameter.NoValuesException(
                "Values vector '{vec}' is too short ({len})".format(
                    vec=self.values, len=len(self.values)))

    def gen_line(self):
        """
        Generates all parameter values in order of addition.
        """
        for value in self.values:
            yield {self.name: value}

    def gen_edges(self):
        """
        Generates edge values of the parameter.
        """
        if len(self.values) == 1:
            yield {self.name: self.values[0]}
        else:
            yield {self.name: self.values[0]}
            yield {self.name: self.values[-1]}

    def gen_collapse(self):
        """
        Generates all parameter values ordered from edges towards center.
        """
        values = self.values
        while True:
            if values:
                yield {self.name: values.pop(0)}
            else:
                break
            if values:
                yield {self.name: values.pop(-1)}
            else:
                break
