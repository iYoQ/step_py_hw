#!/usr/bin/env python

from os import strerror

def start():
    try:
        path = input('path to file: ')
        with open(path, 'r') as f:
            text = f.read()
        with open(path, 'w') as f:
            f.write(text.replace(input('input find word: '), input('input new word: ')))
    except IOError as e:
        print('error:', strerror(e.errno))

if __name__ == '__main__':
    start()