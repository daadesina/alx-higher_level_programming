#!/usr/bin/python3

class Rec:
    def __init__(self, age):
        self.__age = age

    def __str__(self):
        return self.__age * 2

    def __repr__(self):
        print("Hey")
        return "Rectangle(" + self.__age + ")"

ade = Rec("5");
#print (eval(repr(ade)))

print(repr(ade))
