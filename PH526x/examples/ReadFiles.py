# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:06:44 2021

@author: Admin
"""

with open("input.txt", "w") as file:
    file.write("Hello\nWorld")
    file.write('\nNguyen Le Minh An')
# F.close()
lines = []
for line in open("input.txt"):
    lines.append(line.strip())
print(lines)
