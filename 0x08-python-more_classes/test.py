#!/usr/bin/python3

class Rec:
    mymy = "#"
    def __init__(self, age):
        self.__age = age
        Rec.mymy = self.mymy

    def __str__(self):
        return self.mymy

    def __repr__(self):
        print(Hey)
        return "Rectangle(" + self.__age + ")"

ade = Rec("5");

ade.mymy = "c"

print(ade)
