#!/usr/bin/env python
from functools import singledispatchmethod

W_INPUT = 'wrong input'


class Employee():
    def __init__(self, first:str='test_name', last:str='test_lastName', pay:int=20000):
        self.__first = first
        self.__last = last
        self._pay = pay

    @property
    def email(self):
        return f'{self.__first}.{self.__last}@email.com'
    @email.setter
    def email(self, text):
        self.__first, self.__last = text.split()
    @email.deleter
    def email(self):
        self.__first = None
        self.__last = None

    def apply_raise(self, raise_amt):
        self._pay = int(self._pay * (1+raise_amt))

    def __str__(self):
        return f'name: {self.__first} last: {self.__last} pay: {self._pay}'

    @property
    def fullname(self):
        return f'{self.__first} {self.__last}'

class Director(Employee):
    def __init__(self, first:str='test_name', last:str='test_lastName', pay:int=20000):
        super().__init__(first, last, pay)
        self.sub = []

    def __str__(self):
        return f'{self.fullname} \nEmployee: {", ".join(map(lambda employee: employee.fullname, self.sub))}'

    @singledispatchmethod
    def hire(self, first=None, last=None, position=None, pay=None, prog_lang=None):
        print(W_INPUT)

    @hire.register
    def _(self, first:str, last:str, position, pay, prog_lang=None):
        if position == Developer:
            self.sub.append(position(first, last, pay, prog_lang))
        elif position == Support:
            self.sub.append(position(first, last, pay))
        else:
            print(W_INPUT)

    @hire.register
    def _(self, obj:Employee):
        self.sub.append(obj)

    @singledispatchmethod
    def dismiss(self, first=None, last=None):
        print(W_INPUT)

    @dismiss.register
    def _(self, first:str, last:str):
        for obj in self.sub:
            if obj.fullname == f'{first} {last}':
                self.sub.remove(obj)
                return f'dissmis {obj.fullname}'
        return 'no found'

    @dismiss.register
    def _(self, obj:Employee):
        if obj in self.sub:
            self.sub.remove(obj)
            return f'dissmis {obj.fullname}'
        return 'no found'

class Developer(Employee):

    __raise_amt = 0.05

    def __init__(self, first:str='test_name', last:str='test_lastName', pay:int=20000, prog_lang='py'):
        super().__init__(first, last, pay)
        self.prog = prog_lang

    def apply_raise(self):
        super().apply_raise(Developer.__raise_amt)

    @property
    def fulldeveloper(self):
        return f'{super().fullname} {self.prog} {self._pay}'

class Support(Employee):

    __raise_amt = 0.02

    def __init__(self, first:str='test_name', last:str='test_lastName', pay:int=20000):
        super().__init__(first, last, pay)

    def apply_raise(self):
        super().apply_raise(Support.__raise_amt)

    @property
    def fullsupport(self):
        return f'{super().fullname} {self._pay}'


if __name__ == '__main__':
    
    def test_hire_and_dismiss_by_name():
        director = Director('Jane', 'Doe')
        director.hire('John', 'Doe', Developer, 40000, 'c')

        print(director)

        director.dismiss('John', 'Doe')
        print(director)



    def test_hire_and_dismiss_by_obj():
        director = Director('Jane', 'Doe')
        support = Support()

        
        director.hire(support)
        print(director)
        
        director.dismiss(support)
        print(director)


    test_hire_and_dismiss_by_name()
    test_hire_and_dismiss_by_obj()
