#!/usr/bin/env python3

from random import randint 
import operator

# task 1
exp = input("input expression ")

if "+" in exp:
    x, y = exp.split("+")
    print(int(x) + int(y))
elif "-" in exp:
    x, y = exp.split("-")
    print(int(x) - int(y))
elif "*" in exp:
    x, y = exp.split("*")
    print(int(x) * int(y))
elif "/" in exp:
    x, y = exp.split("/")
    print(int(x) / int(y))
else:
    print("whats wrong")

# task 1.2
def func (x, comp, y):
    opers = {"+" : operator.add,
             "-" : operator.sub,
             "*" : operator.mul,
             "/" : operator.truediv}
    return opers[comp](x, y)
    
exp = input("input expression ")

for i in exp:
    if not i.isalnum():
        exp = exp.split(i)
        if len(exp) != 2:
            print("input >2 numbers")
            break
        print(func(int(exp[0]), i, int(exp[1])))
        break


# task 2
list_ = [randint(-10, 10) for i in range(10)]
count_pos = 0
count_neg = 0
count_zer = 0

for i in list_:
    if i > 0:
        count_pos += 1
    if i < 0:
        count_neg += 1
    if i == 0:
        count_zer += 1
        
print(f"{list_}\nnumber of positive: {count_pos}\nnumber of negative: {count_neg}\nnumber of zero: {count_zer}\nmax: {max(list_)}\nmin: {min(list_)}")

