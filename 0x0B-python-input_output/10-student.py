#!/usr/bin/python3
'''A module'''


class Student:
    '''A class'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        result = {}

        if attrs is None:
            return (self.__dict__)

        for i in attrs:
            value = self.__dict__.get(i)
            if value is not None:
                result[i] = value

        return result
