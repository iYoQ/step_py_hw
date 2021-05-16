#!/usr/bin/env python

class Man:
    def __init__(self, name='test name', birthday='test birthday', tel='test tel', city='test city', country='test country', address='test address'):
        self.__name = name
        self.__birthday = birthday
        self.__tel = tel
        self.__city = city
        self.__country = country
        self.__address = address

    def print_(self):
        for i in (tmp := vars(self)):
            print(tmp[i])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
