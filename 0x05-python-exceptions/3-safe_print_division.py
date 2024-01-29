#!/usr/bin/python3
'''collect two integers a and b
    try d = a/b
    except ZeroDivisionError if failed
    else print(d)
    finally: print("Inside result")'''


def safe_print_division(a, b):
    try:
        d = a/b
    except ZeroDivisionError:
        return None
    else:
        return (d)
    finally:
        if b != 0:
            print("Inside result: {}".format(d))
        else:
            print("Inside result: None")
