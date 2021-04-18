#!/usr/bin/env python

INPUT_WORD = "input word: "
NOT_IN_DICT = "not in dict"


def add(eng_fr_dict):
    add_word = input(INPUT_WORD)
    if add_word in eng_fr_dict:
        print("alredy in dict")
    else:
        add_translate = input("input translate: ")
        eng_fr_dict[add_word] = add_translate
        print("add new translate")

def delete(eng_fr_dict):
    del_word = input(INPUT_WORD)
    if del_word in eng_fr_dict:
        del eng_fr_dict[del_word]
        print("delete translate")
    else:
        print(NOT_IN_DICT)

def search(eng_fr_dict):
    srch_word = input(INPUT_WORD)
    if srch_word in eng_fr_dict:
        print(f"translate of {srch_word}: {eng_fr_dict[srch_word]}")
    else:
        print(NOT_IN_DICT)

def change(eng_fr_dict):
    change_translate = input(INPUT_WORD)
    if change_translate in eng_fr_dict:
        new_translate = input("input new translate: ")
        eng_fr_dict[change_translate] = new_translate
        print(f"translate of {change_translate} has changed")
    else:
        print(NOT_IN_DICT)

def menu(ch, eng_fr_dict):
    if ch == 1:
        add(eng_fr_dict)
    elif ch == 2:
        delete(eng_fr_dict)
    elif ch == 3:
        search(eng_fr_dict)
    elif ch == 4:
        change(eng_fr_dict)
    else:
        print("wrong input")


def start():
    eng_fr_dict = {"Hello":"Bonjour", "world":"monde", }

    while True:
        try:
            ch = int(input("\n1 - add\n2 - delete\n3 - search\n4 - change\n5 - exit\n"))
        except ValueError as no_int:
            print("wrong input", no_int)
            continue

        if ch == 5:
            break

        menu(ch, eng_fr_dict)


if __name__ == "__main__":

    start()
