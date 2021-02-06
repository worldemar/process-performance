#!/usr/bin/env python3


class Parameter():
    class NoValuesException(RuntimeError):
        pass
    class NonStringNameException(RuntimeError):
        pass

    def __init__(self, name=None, values=None):
        self.name = name
        self.values = list(values)
        if not isinstance(name, str):
            raise Parameter.NonStringNameException(
                "Parameter name '{name}' is not string".format(name=name))
        if len(values) < 1:
            raise Parameter.NoValuesException(
                "Values vector '{vec}' is too short ({len})".format(vec=values, len=len(values)))

    def line(self):
        for v in self.values:
            yield v

    def edges(self):
        yield self.values[0]
        yield self.values[-1]

    def collapse(self):
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

if __name__ == '__main__':
    p = Parameter(name="foo", values=[])
