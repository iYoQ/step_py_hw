#!/usr/bin/env python

import sys
import pickle
from os import strerror
from random import choice


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

def start_game():
    try:
        with open('words.txt', 'r') as words:
            word = choice(words.read().lower().split())
        answer = ['_' for _ in word]
        wrong_letters = set()
        game(answer, word, wrong_letters)
    except IOError as e:
        print('error:', strerror(e.errno))

def game(answer:list, word, wrong_letters, max_count_try=6, user_count_try=0):
    while user_count_try < max_count_try:
        print_stat(answer, wrong_letters, user_count_try)

        user_choice = user_input(wrong_letters, answer)
        if user_choice in word:
            for index, letter in enumerate(word):
                if letter == user_choice:
                    answer[index] = user_choice
        else:
            wrong_letters.add(user_choice)
            user_count_try += 1

        if '_' not in answer:
            print_stat(answer, wrong_letters, user_count_try)
            print(f'answer: {word}. you win\n')
            break

    else:
        print_stat(answer, wrong_letters, user_count_try)
        print(f'answer: {word}. you loose\n')

    print_output(word, user_count_try, max_count_try)

    if again(): 
        start_game()

def user_input(wrong_letters, answer:list):
    while True:
        user_choice = input('input one letter: ').lower()
        if len(user_choice) > 1:
            print('input only one letter')
            continue
        if user_choice in wrong_letters or user_choice in answer:
            print('use ANOTHER letter')
            continue
        return user_choice
    
def print_stat(answer:list, wrong_letters, user_count_try):
    try:
        with open('pic', 'rb') as pic:
            hman = pickle.load(pic)
            print(hman[user_count_try])
    except IOError as e:
        print(strerror(e.errno), '- no img file')
    print('wrong letters:', *wrong_letters)
    print(*answer, '\n')


def print_output(word, user_count_try, max_count_try):
    with open('result.txt', 'a') as result:
        if user_count_try == max_count_try:
            print(f'word: {word}, result: loose', file=result)
        else:
            print(f'word: {word}, result: win, mistake count: {user_count_try}', file=result)

def again():
    while True:
        ex = input('again?(y/n) ')
        if ex == 'y':
            return True
        if ex == 'n':
            return False
        print('wrong input')

if __name__ == '__main__':
    start_menu()
