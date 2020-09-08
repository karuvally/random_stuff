#!/usr/bin/env python3
# Do some super testing


class Animal:
    def __init__(self):
        self.is_plant = False

    def speak():
        print("Animals produce wide variety of sounds...")

class Dog(Animal):
    def __init__(self):
       self.no_of_legs = 4
       self.can_run = True
       self.can_jump = True

    def speak():
        print("Bow Bow, I am the dog of wisdom!")

class GoldenRetriever(Dog):
    def __init(self, name):
        self.color = "Gold (duh!)"
        self.is_cute = True
        self.name = name

    def fetch():
        print("Here is the stick you threw, -")


# The function where everything happens
def main():
    # Lets create a GoldenRetriever object
    sparky = GoldenRetriever("Sparky")

