#!/usr/bin/python3

'''
- create a new_list
- if len(list1) == len(list2): do the exceution
- try: ...
- For loop to get the elements
- divide each elemen and store the value in new_list
- except ZeroDivisionError:
    print("division by 0")
- except NameError:
    print(wrong type)
- else: print("out of range") '''


def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    try:
        for i in range(list_length):
            try:
                try:
                    d = [my_list_1[i] / my_list_2[i], ]
                    my_list = my_list + d
                except (TypeError):
                    my_list = my_list + [0,]
                    print("wrong type")
                finally:
                    pass
            except ZeroDivisionError:
                print("division by 0")
            finally:
                pass

    except IndexError:
        my_list = my_list + [0,]
        print("out of range")
    finally:
        return (my_list[:list_length])
