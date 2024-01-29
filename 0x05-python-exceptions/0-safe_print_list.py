#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        word = ""
        for i in new_list:
            word = word + str(new_list[i-1])

        num = int(word)
    except Exception as err:
        return -1
    else:
        print(num)
        if (x <= i):
            return (x)
        else:
            return (i)
