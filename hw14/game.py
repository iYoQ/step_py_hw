#!/usr/bin/env python

from os import strerror
from random import choice
import sys


def print_stat(answer:list, wrong_letters:set):
    print('wrong letters:', *wrong_letters)
    print(*answer)

def print_output(word, user_count_try, max_count_try):
    with open('result.txt', 'a') as result:
        if user_count_try == max_count_try:
            print(f'word: {word}, result: loose', file=result)
        else:
            print(f'word: {word}, result: win, try count: {user_count_try}', file=result)

def again():
    while True:
        ex = input('again?(y/n) ')
        if ex == 'y':
            start_game()
            break
        elif ex == 'n':
            break
        else:
            print('wrong input')

def user_input(answer:list, word, max_count_try = 6):
    user_count_try = 0
    tmp = ''
    wrong_letters = set()

    while user_count_try < max_count_try:
        print_stat(answer, wrong_letters)

        user_choice = input('input one letter: ')
        if len(user_choice) > 1:
            print('input only 1 letter')
            continue
        if user_choice == tmp:
            print('use ANOTHER letter')
            continue
        tmp = user_choice

        if user_choice in word:
            for index, letter in enumerate(word):
                if letter == user_choice:
                    answer[index] = user_choice
        else:
            wrong_letters.add(user_choice)
            user_count_try += 1

        if '_' not in answer:
            print_stat(answer, wrong_letters)
            print('word:', ''.join(answer), 'you win')
            break

    else:
        print_stat(answer, wrong_letters)
        print('answer:', word, '.you loose')

    print_output(word, user_count_try, max_count_try)
    again()

def start_game():
    try:
        with open('words.txt', 'r') as words:
            word = choice(words.read().split())
    except IOError as e:
        print('error:', strerror(e.errno))
    answer = ['_' for i in word]
    user_input(answer, word)

def start_menu():
    while True:
        menu = input('1 - game\n2 - results\n3 - exit\n')
        if menu == '1':
            start_game()
        elif menu == '2':
            try:
                with open('result.txt', 'r') as result:
                    print(result.read())
            except IOError as e:
                print(strerror(e.errno), '/ stats is empty.')
        elif menu == '3':
            sys.exit()
        else:
            print('wrong input')

if __name__ == '__main__':
    start_menu()
