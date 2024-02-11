#!/usr/bin/python3
'''A module'''



class Base:
    '''A class'''

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def validator(self, name, *argv):
        for i in argv:
            if type(argv) is not int:
                raise TypeError(f'{name} must be an integer')

            if i <= 0:
                raise ValueError(f'{name} must be > 0')
