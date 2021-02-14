#!/usr/bin/env python
"""
    Usege example.
    Edit parameters to suit your need and run!
"""

from process_performance.parameters import Parameters, cmdline_gen


def main():
    param = Parameters({
        'p1': [0, 3, 'z', 's', 'k', 'l', 'm'],
        'p2': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'p3': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    })
    cmd = ['command.exe', '-O{p1}', '-f', 'p2={p2},p3={p3}']
    for line in cmdline_gen(parameters=param, cmd=cmd, shape='fill'):
        print(line)


if __name__ == '__main__':
    main()
