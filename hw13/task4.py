#!/usr/bin/env python

from os import strerror

def find_max_len(file):
    lines = file.readlines()
    lines = map(lambda x: x.replace(' ', '').strip(), lines)
    print(f'max lenght line: {len(max(lines))}')

def start():
    try:
        with open(input('path to file: '), 'r') as f:
            find_max_len(f)
    except IOError as e:
        print('error:', strerror(e.errno))

if __name__ == '__main__':
    start()