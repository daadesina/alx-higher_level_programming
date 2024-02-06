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

    def reload_from_json(self, json):

        dict_des = self.__dict__

        for key, value in json.items():
            if (dict_des.get(key) == self.first_name):
                self.first_name = value
            elif (dict_des.get(key) == self.last_name):
                self.last_name = value
            elif (dict_des.get(key) == self.age):
                self.age = value
