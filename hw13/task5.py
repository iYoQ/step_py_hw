#!/usr/bin/env python

from os import strerror

def count_word(file, word):
    print(sum(1 for i in file.read().split() if i == word))

def start():
    try:
        with open(input('path to file: '), 'r') as f:
            count_word(f, input('input search word: '))
    except IOError as e:
        print('error:', strerror(e.errno))

if __name__ == '__main__':
    start()