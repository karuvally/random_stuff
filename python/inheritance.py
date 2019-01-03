#!/usr/bin/env python3

class ClassWithVars:
    def __init__(self):
        self.first_variable = 4
        self._second_variable = 5
        self.__third_variable = 6


class DerivedClass(ClassWithVars):
    def print_values(self):
        print(self.first_variable)
        print(self._second_variable)
        # print(self.__third_variable)


instance = DerivedClass()
instance.print_values()
