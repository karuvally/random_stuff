#!/usr/bin/env python3
# Copyright 2018, Aswin Babu Karuvally, Tharun P Karun

# check if a number is angstrom
def check_angstrom(number):
    # essential variables
    sum_of_cubes = 0
    original_number = number
    
    while number > 0:
        sum_of_cubes += (number % 10) ** 3
        number = int(number / 10)

    if original_number == sum_of_cubes:
        return True
    
    return False
