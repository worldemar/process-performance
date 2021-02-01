#!/usr/bin/python

import itertools

class Dimension(object):
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

class Space(object):
    def __init__(self):
        self.dimensions = {}
    def add_dim(self, name, values):
        self.dimensions[name] = Dimension(values)
    def add_strdim(self, name, values):
        self.dimensions[name] = Dimension("%s=%s" % (name, v) for v in values)
    def cube_gen_line_by_line(self):
        for line in self.dimensions.keys():
            values = []
            for edge in self.dimensions.keys():
                if edge == line:
                    continue
                values.append([
                    self.dimensions[edge].values[0],
                    self.dimensions[edge].values[-1]
                    ])
            values.append(self.dimensions[line].values)
            values = itertools.product(*values)
            for v in values:
                yield v
    def cube_gen(self):
        # corners
        values = []
        for dim in self.dimensions.keys():
            values.append([
                self.dimensions[dim].values[0],
                self.dimensions[dim].values[-1]
                ])
        values = itertools.product(*values)
        for v in values:
            yield v
        # edges
        for line in self.dimensions.keys():
            values = [self.dimensions[line].values[1:-1]]
            for edge in self.dimensions.keys():
                if edge == line:
                    continue
                values.append([
                    self.dimensions[edge].values[0],
                    self.dimensions[edge].values[-1]
                    ])
            values = itertools.product(*values)
            for v in values:
                yield v
    def gen(self):
        values = []
        for dim in self.dimensions.keys():
            values.append(self.dimensions[dim].values)
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
