#!/usr/bin/python3
'''A module'''


import json


def save_to_json_file(my_obj, filename):
    '''A function'''

    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
