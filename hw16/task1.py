#!/usr/bin/env python

class Car:
    def __init__(self, model='test model', year='test year', manufacturer='test manufacturer',
                 engine_capacity='test engine', colour='test colour', price='test price'):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__colour = colour
        self.__price = price

    def __str__(self):
        return f'{", ".join(map(str, vars(self).values()))}'

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, val):
        self.__model = val

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, val):
        self.__year = val

    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, val):
        self.__manufacturer = val

    @property
    def engine_capacity(self):
        return self.__engine_capacity
    @engine_capacity.setter
    def engine_capacity(self, val):
        self.__engine_capacity = val

    @property
    def colour(self):
        return self.__colour
    @colour.setter
    def colour(self, val):
        self.__colour = val

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, val):
        self.__price = val
