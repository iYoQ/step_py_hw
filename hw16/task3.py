#!/usr/bin/env python

class Stadium:
    def __init__(self, name='test name', open_date='test open date', country='test country',
                 town='test town', capacity='test capacity'):
        self.__name = name
        self.__open_date = open_date
        self.__country = country
        self.__town = town
        self.__capacity = capacity

    def __str__(self):
        return f'{", ".join(map(str, vars(self).values()))}'

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def open_date(self):
        return self.__open_date
    @open_date.setter
    def open_date(self, val):
        self.__open_date = val

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, val):
        self.__country = val

    @property
    def town(self):
        return self.__town
    @town.setter
    def town(self, val):
        self.__town = val

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, val):
        self.__capacity = val
