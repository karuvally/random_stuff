#!/usr/bin/env python3

# Import libraries
import csv


# Get 2D array without the third element 
def sliced_array(input_csv):
    # The 2D array which we are going to build
    output_array = []

    csv_reader = csv.reader(open(input_csv), delimiter=" ")
    for line in csv_reader:
        # Values enclosed in [] to make array 2D 
        output_array.append([line[0], line[1]])
    
    return output_array


# Get 2D array with x,y values combined
def combined_array(input_csv):
    # Variable to store generated combined array
    output_array = []

    csv_reader = csv.reader(open(input_csv), delimiter=" ")
    for line in csv_reader:
        # x and y values joined with comma as seperator
        output_array.append([",".join((line[0], line[1])), line[2]])

    return output_array

