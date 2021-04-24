#!/usr/bin/env python

def task_1(tuple_1, tuple_2, tuple_3):
    return filter(lambda x: x in tuple_2 and x in tuple_3, set(tuple_1))


def task_2(tuple_1, tuple_2, tuple_3):
    tmp = tuple_1 + tuple_2 + tuple_3
    return filter(lambda x: tmp.count(x) == 1, tmp)

def task_3(tuple_1, tuple_2, tuple_3):
    # tmp = map(set, zip(tuple_1, tuple_2, tuple_3))
    # return filter(lambda x: len(x) == 1, tmp)
    tmp = list(zip(tuple_1, tuple_2, tuple_3))
    return [x for (x, y, z) in tmp if x == y == z]
    
def start():
    tuple_1 = (1, 3, 5, 4, 2, 10, 10, 10, 10)
    tuple_2 = (4, 3, 7, 4, 1, 10, 10, 10)
    tuple_3 = (1, 3, 6, 4, 9, 10, 10)
    print("task 1:", *task_1(tuple_1, tuple_2, tuple_3))
    print("task 2:", *task_2(tuple_1, tuple_2, tuple_3))
    print("task 3:", *task_3(tuple_1, tuple_2, tuple_3))

if __name__ == "__main__" :
    start()
