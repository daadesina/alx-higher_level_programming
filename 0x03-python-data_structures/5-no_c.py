#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new = new + i
    return (new)
