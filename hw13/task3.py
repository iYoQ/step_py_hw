#!/usr/bin/env python

from os import strerror

def del_last_string(file):
    lines = file.readlines()
    if lines[-1] == '\n':
        lines.pop(-2)
    else:
        lines.pop()
    with open('output.txt', 'w') as f_out:
        print(''.join(lines), file=f_out)

def start():
    try:
        with open(input('path to file: '), 'r') as f:
            del_last_string(f)
    except IOError as e:
        print('error:', strerror(e.errno))

if __name__ == '__main__':
    start()