#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = my_list[:x]
    word = ""
    word = word + str(int(my_list[0]))
    list_count = 0
    word_count = 0
    for i in new_list:
        try:
            word = word + str(int(new_list[i]))
        except Exception:
            continue

    num = int(word)

    for j in my_list:
        list_count = list_count + 1

    for k in word:
        word_count = word_count + 1

    if x <= list_count:
        print("{:d}".format(num))
        return (word_count)
    else:
        print("{:d}".format(num), end="")
        raise IndexError('list index out of range')
