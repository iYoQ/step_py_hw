#!/usr/bin/env python

def task_1(tuple_1, tuple_2, tuple_3):
    return filter(lambda x: x in tuple_2 and x in tuple_3, tuple_1)


def task_2(tuple_1, tuple_2, tuple_3):
    tmp = tuple_1 + tuple_2 + tuple_3
    return filter(lambda x: tmp.count(x) == 1, tmp)

def task_3(tuple_1, tuple_2, tuple_3):
    tmp = task_1(tuple_1, tuple_2, tuple_3)
    return filter(lambda x: tuple_1.index(x) == tuple_2.index(x) == tuple_3.index(x), tmp)

def start():
    tuple_1 = (1, 3, 5, 9, 10, 11)
    tuple_2 = (3, 4, 6, 9, 10, 1)
    tuple_3 = (7, 2, 3, 9, 10)
    print("task 1:", *task_1(tuple_1, tuple_2, tuple_3))
    print("task 2:", *task_2(tuple_1, tuple_2, tuple_3))
    print("task 3:", *task_3(tuple_1, tuple_2, tuple_3))

if __name__ == "__main__" :
    start()
