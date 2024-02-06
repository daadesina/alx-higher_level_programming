#!/usr/bin/python3
'''A module'''


import json


def load_from_json_file(filename):
    '''A function'''

    with open(filename, 'r', encoding='utf-8') as my_file:
        return (json.loads(my_file.read()))
