#!/usr/bin/env python3
# Do some testing without super


class Animal:
    def __init__(self):
        self.is_plant = False

    def speak(self):
        print("Animals produce wide variety of sounds...")

class Dog(Animal):
    def __init__(self):
       self.no_of_legs = 4
       self.can_run = True
       self.can_jump = True

    def speak(self):
        print("Bow Bow, I am the dog of wisdom!")

class GoldenRetriever(Dog):
    def __init__(self, name):
        self.color = "Gold (duh!)"
        self.is_cute = True
        self.name = name

    def fetch(self):
        print("Here is the stick you threw, -")


# The function where everything happens
def main():
    # Lets create a GoldenRetriever object
    sparky = GoldenRetriever("Sparky")

    # Lets try out a method
    sparky.fetch()

    # Lets check the dog's name
    print("The dog's name is", sparky.name)

    # Lets try calling a method in Animal
    # Hint, it gets overriden by Dog
    sparky.speak()


# Call the main function
main()

