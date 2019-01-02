#!/usr/bin/env python3

class ClassWithVars:
    _first_variable = 5
    __second_variable = 6


print(ClassWithVars._first_variable)
print(ClassWithVars.__second_variable)
