#!/usr/bin/env python3
"""
    Parameters class providing generators to iterate over
    multi-dimensional space of several parameters
"""

import itertools
from process_performance.parameter import Parameter


class Parameters():
    """
    Collection of parameters with generator helpers for iterating over
    parameter values space.
    """

    def __init__(self, parameters=None):
        if isinstance(parameters, list):
            self.parameters = parameters
        elif isinstance(parameters, dict):
            self.parameters = []
            for key, val in parameters.items():
                self.parameters.append(Parameter(name=key, values=val))
        else:
            raise RuntimeError('parameters argument must be '
                               + 'dict `{"name":[values]}` '
                               + 'or list `[Parameter]`')

    def gen_cube(self):
        """
            Generates edges of multi-dimensional parameter cube
            including corners.
            This generates corners more than once, they supposed
            to be skipped using value cache.
        """
        for p_line in self.parameters:
            generators = list()
            for p_edge in self.parameters:
                if p_edge == p_line:
                    generators.append(p_line.gen_line())
                else:
                    generators.append(p_edge.gen_edges())
            for value in itertools.product(*generators):
                yield value

    def gen_corners(self):
        """
        Generates corners of multi-dimensional parameter cube.
        """
        generators = [p.gen_edges() for p in self.parameters]
        return itertools.product(*generators)

    def gen_fill(self):
        """
        Generates all possible values of multi-dimensional parameter cube.
        """
        generators = [p.gen_line() for p in self.parameters]
        return itertools.product(*generators)

    def gen(self, name):
        """
        Select generator by its string name.
        """
        return {
            "corners": self.gen_corners,
            "cube": self.gen_cube,
            "fill": self.gen_fill
        }[name]


def cmdline_gen(parameters=None, cmd=None, shape=None):
    """
    Generate command line list from parameters.
    """
    def dictify(value):
        ret = {}
        for d in value:
            ret.update(d)
        return ret
    for param in parameters.gen(shape)():
        param_dict = dictify(param)
        # cmd_formatted = list(arg.format(**param_dict) for arg in cmd)
        cmd_formatted = []
        for arg in cmd:
            cmd_formatted.append(arg.format(**param_dict))
        yield cmd_formatted
