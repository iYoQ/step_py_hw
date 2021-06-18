#!/usr/bin/env python

class Book:
    def __init__(self, name='test name', year='test year', publisher='test publisher',
                 genre='test genre', author='test author', price='test price'):
        self.__name = name
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __str__(self):
        return f'{", ".join(map(str, vars(self).values()))}'

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, val):
        self.__year = val

    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, val):
        self.__publisher = val

    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, val):
        self.__genre = val

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, val):
        self.__author = val

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, val):
        self.__price = val
