# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:00:29 2021

@author: Admin
"""

numbers = range(10)

squares = []

for number in numbers:
    square = number**2
    squares.append(square)

squares2 = [number**2 for number in numbers]

print(squares)
print(squares2)

a = sum([i**2 for i in range(3)])
b = sum([i for i in range(10) if i % 2 == 1])
print(a)
print(b)
