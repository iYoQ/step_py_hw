#!/usr/bin/env python

from os import strerror

def compare(file_1, file_2):
    flag = False
    for num, (line_1, line_2) in enumerate(zip(file_1, file_2)):
        if line_1 != line_2:
            flag = True
            print(f'\ndiff in string: {num+1}\nstring in file 1: {line_1.strip()}\nstring in file 2: {line_2.strip()}\n')
    if not flag:
        print('equal')

def start():
    try:
        with open(input('path for file 1: '), 'r') as f1, open(input('path for file 2: '), 'r') as f2:
            compare(f1, f2)
    except IOError as e:
        print('error:', strerror(e.errno))


if __name__ == '__main__':
    start()