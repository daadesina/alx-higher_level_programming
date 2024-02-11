#!/usr/bin/python3

class mymy:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return (self.__age)

    @age.setter
    def age(self, value):
        self.__age = value


ade = mymy(23)
ade.age = 45
print(ade.age)
