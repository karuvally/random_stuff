#!/usr/bin/env python3

class MyFirstClass:
    def __init__(self, value):
        self.my_first_value = value

    def print_value(self):
        print(self.my_first_value)


def main():
    classInstance = MyFirstClass(5)
    classInstance.print_value()


main()
