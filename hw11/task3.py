#!/usr/bin/env python

INPUT_ID = "input id: "
NOT_IN_FIRM = "not in firm"


def __input_value():
    info_list = []
    template_struct = ["name", "tel", "e-mail", "post", "cabinet", "skype"]

    for i in template_struct:
        info_list.append(input(f"input {i}: "))

    return dict(zip(template_struct, info_list))

def add(firm_dict):
    add_id = input(INPUT_ID)
    if add_id in firm_dict:
        print("alredy in firm")
    else:
        firm_dict[add_id] =  __input_value()
        print("add new employee:", firm_dict[add_id]["name"])

def delete(firm_dict):
    del_id = input(INPUT_ID)
    if del_id in firm_dict:
        del firm_dict[del_id]
        print("delete employee")
    else:
        print(NOT_IN_FIRM)

def search(firm_dict):
    find = False
    srch_empl = input("input info: ")
    for id_ in firm_dict:
        if srch_empl in firm_dict[id_].values() or srch_empl == id_:
            find = True
            print(f"\n\tid: {id_}", end='\n\n')
            for keys, values in firm_dict[id_].items():
                print(f"\t{keys}: {values}")

    if not find:
        print(NOT_IN_FIRM)

def change(firm_dict):
    change_id = input(INPUT_ID)
    if change_id in firm_dict:
        firm_dict[change_id] =  __input_value()
        print("employee", firm_dict[change_id]["name"], "has changed")
    else:
        print(NOT_IN_FIRM)

def menu(ch, firm_dict):
    if ch == 1:
        add(firm_dict)
    elif ch == 2:
        delete(firm_dict)
    elif ch == 3:
        search(firm_dict)
    elif ch == 4:
        change(firm_dict)
    else:
        print("wrong input")


def start():
    firm_dict = {
        "id_1": {
            "name": "John Doe",
            "tel": "7777777777",
            "e-mail": "example@gmail.com",
            "post": "CEO",
            "cabinet": "1",
            "skype": "john777",
        },
        "id_2" : {
            "name": "Jane Doe",
            "tel": "8888888888",
            "e-mail": "example2@gmail.com",
            "post": "manager",
            "cabinet": "2",
            "skype": "jane888",
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

        menu(ch, firm_dict)


if __name__ == "__main__":

    start()
