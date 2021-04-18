#!/usr/bin/env python3


def task1():
    print("“Don't compare yourself with anyone in this world…",
          "if you do so, you are insulting yourself.”",
          "{:>55}".format("Bill Gates"), sep = "\n")

def task2(a, b):
    print(*(i for i in range(a, b + 1) if i % 2 == 0))

def task3(lgt, sym, fill = True):
    if fill:
        for _ in range(lgt):
            print((sym + " ") * lgt)
    else:
        print(sym * lgt)
        for _ in range(2, lgt):
            print(sym, " " * (lgt - 2), sym, sep = "")
        print(sym * lgt)

def task4(*args):
    mini = args[0]
    for i in args:
        mini = i if i < mini else mini
    print(mini)

def task5(start, end):
    p = 1
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        p *= i
    return p

def task6(a):
    a = abs(a)
    count = 0
    while a > 0:
        a //= 10
        count += 1
    return count

def task7(a):
    a = list(map(int, str(a)))
    if len(a) % 2 == 0 or len(a) == 1:
        return True if a == a[::-1] else False
    return False

def task7_1(a):
    tmp_a = a
    rev = 0
    while tmp_a > 0:
        rev = rev * 10 + tmp_a % 10
        tmp_a //= 10
    return True if a == rev else False


if __name__ == "__main__":
    task1()
    # task2(0, 24)
    # task3(5, "*", )
    # task4(20, -5, 2, -10, 120, )
    # print(task5(5, 3))
    # print(task6(-4550))
    # print(task7(123321))
    # print(task7_1(123321))