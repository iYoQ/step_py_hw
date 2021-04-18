#!/usr/bin/env python

INPUT_NAME = "input player name: "
NOT_IN_DICT = "not in dict"


def add(basketball_players):
    add_player = input(INPUT_NAME)
    if add_player in basketball_players:
        print("alredy in dict")
    else:
        add_growth = input("input player growth: ")
        basketball_players[add_player] = add_growth
        print(f"add new player: {add_player}")

def delete(basketball_players):
    del_player = input(INPUT_NAME)
    if del_player in basketball_players:
        del basketball_players[del_player]
        print(f"delete player: {del_player}")
    else:
        print(NOT_IN_DICT)

def search(basketball_players):
    srch_player = input(INPUT_NAME)
    srch = False
    for player in basketball_players:
        if srch_player in player:
            print(f"growth of {player}: {basketball_players[player]}",)
            srch = True
    if not srch:
        print(NOT_IN_DICT)

def change(basketball_players):
    change_player = input(INPUT_NAME)
    if change_player in basketball_players:
        new_growth = input("input new growth: ")
        basketball_players[change_player] = new_growth
        print(f"{change_player} has changed")
    else:
        print(NOT_IN_DICT)

def menu(ch, basketball_players):
    if ch == 1:
        add(basketball_players)
    elif ch == 2:
        delete(basketball_players)
    elif ch == 3:
        search(basketball_players)
    elif ch == 4:
        change(basketball_players)
    else:
        print("wrong input")


def start():
    basketball_players = {"Michael Jordan":"198cm", "LeBron James":"206cm", }

    while True:
        try:
            ch = int(input("\n1 - add\n2 - delete\n3 - search\n4 - change\n5 - exit\n"))
        except ValueError as no_int:
            print("wrong input", no_int)
            continue

        if ch == 5:
            break

        menu(ch, basketball_players)


if __name__ == "__main__":

    start()
