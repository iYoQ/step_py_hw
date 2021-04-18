#!/usr/bin/env python3

import random
import numpy
from colorama import Fore, Style


def __check_row(matr, smb):
    return bool(sum([ True for row in matr if __check_sum_smb(row, smb)]))

def __check_col(matr, smb):
    matr_t = numpy.transpose(matr)
    return __check_row(matr_t, smb)

def __check_diag(matr, smb):
    return \
        sum([ ord(matr[i][i]) for i in range(N)]) == ord(smb)*N or \
        sum([ ord(matr[i][N-i-1]) for i in range(N)]) == ord(smb)*N

def __check_sum_smb(list_, smb, index=None):
    if index is not None:
        return sum( [ord(x[index]) for x in list_]) == ord(smb)*N
    return sum( [ ord(x) for x in list_]) == ord(smb)*N

def __smart_move(matr, smb):
    for k in smb:
        for index, row in enumerate(matr):
            if sum( [ ord(x) for x in row]) == ord(k)*(N - 1) + ord("-"):
                return index + 1
    return random.randint(1, N)

def __smart_diag(matr, smb, rev=True):

    if rev:
        for k in smb:
            if sum([ ord(matr[i][i]) for i in range(N)]) == ord(k)*(N - 1) + ord("-"):
                for j in range(N):
                    if matr[j][j] == "-":
                        return j + 1,j + 1
        return None
    for k in smb:
        if sum([ ord(matr[i][N-i-1]) for i in range(N)]) == ord(k)*(N - 1) + ord("-"):
            for j in range(N):
                if matr[j][N-j-1] == "-":
                    return j + 1, N - j
    return None

def __get_pos(matr, smb, count=0):
    if smb == '*':
        while True:
            try:
                row = int(input('row = '))
                col = int(input('col = '))
                if matr[row-1][col-1] == '-':
                    break

            except ValueError as no_int:
                print("wrong input:", no_int)
            except IndexError:
                print(f"range of board: {N}")
        smb = '0'
    else:
        while True:
            count += 1
            if count == 20:
                row = random.randint(1, N)
                count -= 1
            elif (p_choise := __smart_diag(matr, ("0", "*"))) is not None:
                row, col = p_choise
            elif (p_choise := __smart_diag(matr, ("0", "*"), False)) is not None:
                row, col = p_choise
            else:
                row = __smart_move(matr, ("0", "*"))
                col = __smart_move(numpy.transpose(matr), ("0", "*"))

            if matr[row-1][col-1] == '-':
                break
        smb = '*'
    return row, col, smb

def play_round(matr, smb):
    row, col, new_smb = __get_pos(matr, smb)
    matr[row - 1][col - 1] = smb

    _print(matr)

    if __check_row(matr, smb) or __check_col(matr, smb) or __check_diag(matr, smb):
        if __check_col(matr, smb):
            _print_win_col(matr)

        if smb == '*':
            print('you win')
        else:
            print('you lose')
        return

    if not bool(sum([ '-' in row for row in matr ])):
        print('draw')
        return

    play_round(matr, new_smb)

def _print(matr):
    for row in matr:
        print('\t', end = ' ')
        for value in row:
            if value == '*':
                color = "\033[4m" + Fore.GREEN if __check_sum_smb(row, value) else Fore.GREEN
            elif value == '0':
                color = "\033[4m" + Fore.RED if __check_sum_smb(row, value) else Fore.RED
            else:
                color = Fore.WHITE
            print(color + value, sep='\t', end='\t')
        print(Style.RESET_ALL)
    print(end='\n\n')

def _print_win_col(matr):
    for row in matr:
        print('\t', end = ' ')
        for index, value in enumerate(row):
            if value == '*':
                color = "\033[4m" + Fore.GREEN if __check_sum_smb(matr, value, index) else Fore.GREEN
            elif value == '0':
                color = "\033[4m" + Fore.RED if __check_sum_smb(matr, value, index) else Fore.RED
            else:
                color = Fore.WHITE
            print(color + value, sep='\t', end='\t')
            print(Style.RESET_ALL, sep="", end="")
        print(Style.RESET_ALL)
    print(end='\n\n')

if __name__ == "__main__":
    N = 3
    __matr = [ ['-' for _ in range(N)] for _ in range(N) ]

    play_round(__matr, '*')
