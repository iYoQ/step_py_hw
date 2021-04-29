#!/usr/bin/env python

from os import strerror

def info(file):
    info_dict = {'symbols':0, 'strings':0, 'vowels':0, 'consonants':0, 'numbers':0}
    vowels = "aeuioy"
    for i in file.read():
        if not i.isspace():
            info_dict['symbols'] += 1
        if i.isalpha():
            if i in vowels:
                info_dict['vowels'] += 1
            else:
                info_dict['consonants'] += 1
        if i.isdigit():
            info_dict['numbers'] += 1
        if i == '\n':
            info_dict['strings'] += 1
    return info_dict

def file_print(info_dict):
    with open('info.txt', 'w') as f_out:
        print(info_dict, file=f_out)

def start():
    try:
        with open(input('path to file: '), 'r') as f_in:
            file_print(info(f_in))
    except IOError as e:
        print('error:', strerror(e.errno))


if __name__ == '__main__':
    start()