#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [0] * len(my_list)

    for i in range(len(my_list)):
        new_list[i] = new_list[i] + my_list[i]
        if new_list[i] == search:
            new_list[i] = replace

    return (new_list)
