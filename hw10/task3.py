#!/usr/bin/env python3


from random import randint

def sort_bubble(list_):
    count = 0
    for i in range(1, len(list_)):
        flag = True
        for j in range(len(list_) - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                flag = False
                count += 1
        if flag:
            break
    return list_, count

test_list = [randint(-10, 10) for _ in range(10)]
a, b = sort_bubble(test_list)
print(a, b, sep='\n')
