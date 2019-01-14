#!/usr/bin/env python3

class SecondClass:
    class_variable = 5

    def printout(self):
        print(SecondClass.class_variable)


myInstance = SecondClass()
anotherInstance = SecondClass()

myInstance.printout()
anotherInstance.printout()

