#!/usr/bin/python

import itertools


class Dimension():
    def __init__(self, values):
        self.values = list(values)

    def collapse_gen(self):
        def collapse():
            values = self.values
            while True:
                if values:
                    yield values.pop(0)
                else:
                    break
                if values:
                    yield values.pop(-1)
                else:
                    break
        return collapse


class Space():
    def __init__(self):
        self.dimensions = {}

    def add_dim(self, name, values):
        self.dimensions[name] = Dimension(values)

    def add_strdim(self, name, values):
        self.dimensions[name] = Dimension("%s=%s" % (name, v) for v in values)

    def cube_gen_line_by_line(self):
        for line_name, line_value in self.dimensions.items():
            values = []
            for edge_name, edge_value in self.dimensions.items():
                if edge_name == line_name:
                    continue
                values.append([
                    edge_value.values[0],
                    edge_value.values[-1]
                    ])
            values.append(line_value.values)
            values = itertools.product(*values)
            for v in values:
                yield v

    def cube_gen(self):
        # corners
        values = []
        for _, dim_value in self.dimensions.items():
            values.append([
                dim_value.values[0],
                dim_value.values[-1]
                ])
        values = itertools.product(*values)
        for v in values:
            yield v
        # edges
        for line_name, line_value in self.dimensions.items():
            values = [line_value.values[1:-1]]
            for edge_name, edge_value in self.dimensions.items():
                if edge_name == line_name:
                    continue
                values.append([
                    edge_value.values[0],
                    edge_value.values[-1]
                    ])
            values = itertools.product(*values)
            for v in values:
                yield v

    def gen(self):
        values = []
        for _, dim_value in self.dimensions.items():
            values.append(dim_value.values)
        values = itertools.product(*values)
        for v in values:
            yield v


if __name__ == '__main__':
    s = Space()
    # s.add_strdim("L=", ["a", "b", "c", "d"])
    # s.add_strdim("N=", [1, 2, 3, 4])
    # s.add_strdim("D=", [".", ":", "!", "|"])
    s.add_strdim("N=", [1, 2, 3, 4])
    s.add_strdim("X=", ["A", "B", "C", "D"])
    s.add_strdim("T=", ["X", "Y", "Z", "T"])
    for v in s.cube_gen_line_by_line():
        if v:
            print(sorted(v))
        else:
            print()
