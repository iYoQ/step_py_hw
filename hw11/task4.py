#!/usr/bin/env python

INPUT_ID = "input id: "
NOT_IN_COLLECT = "not in collect"


def __input_value():
    info_list = []
    template_struct = ["autor", "tittle", "genre", "year", "num_of_pages", "publisher"]

    for i in template_struct:
        info_list.append(input(f"input {i}: "))

    return dict(zip(template_struct, info_list))

def add(books_collect):
    add_id = input(INPUT_ID)
    if add_id in books_collect:
        print("alredy in collect")
    else:
        books_collect[add_id] =  __input_value()
        print("add new book:", books_collect[add_id]["tittle"])

def delete(books_collect):
    del_id = input(INPUT_ID)
    if del_id in books_collect:
        del books_collect[del_id]
        print("delete book")
    else:
        print(NOT_IN_COLLECT)

def search(books_collect):
    find = False
    srch_book = input("input info: ")
    for id_ in books_collect:
        if srch_book in books_collect[id_].values() or srch_book == id_:
            find = True
            print(f"\n\tid: {id_}", end='\n\n')
            for keys, values in books_collect[id_].items():
                print(f"\t{keys}: {values}")

    if not find:
        print(NOT_IN_COLLECT )

def change(books_collect):
    change_id = input(INPUT_ID)
    if change_id in books_collect:
        books_collect[change_id] =  __input_value()
        print("book", books_collect[change_id]["tittle"], "has changed")
    else:
        print(NOT_IN_COLLECT)

def menu(ch, books_collect):
    if ch == 1:
        add(books_collect)
    elif ch == 2:
        delete(books_collect)
    elif ch == 3:
        search(books_collect)
    elif ch == 4:
        change(books_collect)
    else:
        print("wrong input")


def start():
    books_collect = {
        "id_1": {
            "autor": "John Doe",
            "tittle": "some book",
            "genre": "detective",
            "year": "1994",
            "num_of_pages": "500",
            "publisher": "some publisher",
        },
        "id_2" : {
            "autor": "Jane Doe",
            "tittle": "another some book",
            "genre": "novel",
            "year": "1996",
            "num_of_pages": "657",
            "publisher": "another some publisher",
        },

    }

    while True:
        try:
            ch = int(input("\n1 - add\n2 - delete\n3 - search\n4 - change\n5 - exit\n"))
        except ValueError as no_int:
            print("wrong input:", no_int)
            continue

        if ch == 5:
            break

        menu(ch, books_collect)


if __name__ == "__main__":

    start()
