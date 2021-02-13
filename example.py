#!/usr/bin/env python
"""
    Usege example.
    Edit parameters to suit your need and run!
"""

from process_performance.parameters import Parameters, cmdline_gen

if __name__ == '__main__':
    p = Parameters({
        'p1': [0, 3, 'z', 's'],
        'p2': [3, 4, 5],
        'p3': [7, 8, 9]
    })
    c = ['command.exe', '-O{p1}', '-f', 'p2={p2},p3={p3}']
    for line in cmdline_gen(parameters=p, cmd=c, shape='cube'):
        print(line)
