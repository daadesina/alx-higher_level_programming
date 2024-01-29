#!/usr/bin/python3
def uniq_add(my_list=[]):
    setList = list(set(my_list))
    new_list = []
    add = 0

    for i in range(len(setList)):
        new_list.append(setList[i])
        add = add + setList[i]

    return (add)
