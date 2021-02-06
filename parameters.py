#!/usr/bin/env python3

import itertools
from parameter import Parameter


class Parameters():
    """
    Collection of parameters with generator helpers for iterating over
    parameter values space.
    """

    def __init__(self, parameters=None):
        self.parameters = parameters

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


if __name__ == '__main__':
    p1 = Parameter("p1", [1, 2, 3])
    p2 = Parameter("p2", [4, 5, 6])
    p3 = Parameter("p3", [7, 8, 9])
    p = Parameters([p1, p2, p3])
    for v in p.gen_cube():
        print(v)
