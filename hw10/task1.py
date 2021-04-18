#!/usr/bin/env python3.9

from random import randint

def check_avr(list_):
    s = sum(list_)/len(list_)
    print("avr:", s)
    return s

def sort_(list_, len_list):
    comb = int(len_list // 1.247)
    for i in range(comb, 0, -1):
        for j in range(len_list - 1):
            if j+i < len_list and list_[j] > list_[j + i]:
                list_[j], list_[j + i] = list_[j + i], list_[j]
    list_[len_list:] = list_[:len_list-1:-1]
    return list_

def get_list(list_):
    len_list = int(len(list_) * 2/3) if check_avr(list_) > 0 else int(len(list_) * 1/3)
    sort_(list_, len_list)
    return list_

if __name__ == "__main__":
    _list = [randint(-10, 10) for _ in range(20)]
    print(_list)
    print(get_list(_list))
