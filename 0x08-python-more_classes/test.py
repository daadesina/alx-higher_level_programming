#!/usr/bin/python3
"""A module of a class
"""


class Rectangle:
    def __init__(self, name):
        self.__name = name

    @property
    def mymy(self):
        return self.__name

    @mymy.setter
    def mymy(self, name):
        self.__name = name;

ade = Rectangle("adesin")
print(ade.mymy)
