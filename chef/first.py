#!/usr/bin/env python3

array = []

while True:
    temp = int(input())
    if temp != 42:
        array.append(temp)
    else:
        break

for number in array:
    print(number)