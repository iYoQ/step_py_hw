#!/usr/bin/env python3

import os
import operator


W_INP = "wrong input"

def __print(list_grades):
    print("list of grades:")
    return list_grades

def __retake(list_grade):
    print("list of grade:", *list_grade)
    while True:
        try:
            num_of_ex = int(input("input num of exam(1-10): "))
            new_grade = int(input("input new grade(0-12): "))
        except ValueError as err:
            print(W_INP, err)
            continue
        if 0 <= new_grade <= 12 and 0 < num_of_ex <= 10:
            if len(list_grade) >= num_of_ex > 0:
                list_grade[num_of_ex - 1] = new_grade
            else:
                list_grade.append(new_grade)
            return list_grade
        print(W_INP)

def __check_grant(list_grade):
    avr_of_grade = sum(list_grade) / len(list_grade)
    return "\nyes" if avr_of_grade > 10.7 else "\nno"

def __sort(list_grade, comp):
    comb = int(len(list_grade) // 1.247)
    tmp_list = list_grade.copy()

    for i in range(comb, 0, -1):
        for j in range(len(tmp_list) - 1):
            if j+i < len(tmp_list) and comp(tmp_list[j], tmp_list[j + i]):
                tmp_list[j], tmp_list[j + i] = tmp_list[j + i], tmp_list[j]
    return tmp_list

def __menu(menu_choise, list_grade):
    if menu_choise == 1:
        return __print(list_grade)
    if menu_choise == 2:
        return __retake(list_grade)
    if menu_choise == 3:
        return __check_grant(list_grade)
    if menu_choise == 4:
        while True:
            try:
                c_sort = float(input("4.1 - sort ascending\n4.2 - sort descending\n"))
            except ValueError as err:
                print(W_INP, err)
                continue
            if c_sort == 4.1:
                return __sort(list_grade, operator.gt)
            if c_sort == 4.2:
                return __sort(list_grade, operator.lt)
            print(W_INP)
    return W_INP

def __input_list_grades():
    while True:
        try:
            _list_grades = [int(x) for x in input("input ten grades(0-12): ").split()[:10]]
        except ValueError as err:
            print(W_INP, err)
            continue

        for i in _list_grades:
            if i < 0 or i > 12:
                print(W_INP)
                break
        else:
            return _list_grades

def _start():
    list_grades = __input_list_grades()
    while True:
        try:
            choise = int(input("\n   ----menu----\n\n1 - list of grades\n2 - retake exam\n3 - average grades\n4 - sort grades\n5 - exit\n"))
        except ValueError as err:
            print(W_INP, err)
            continue
        if choise == 5:
            print("exit")
            break
        print(*__menu(choise, list_grades))
        os.system("pause")

if __name__ == "__main__":

    _start()
