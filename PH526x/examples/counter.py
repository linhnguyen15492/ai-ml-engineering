# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:43:50 2021

@author: admin
"""

sentence = input('Write your sentences: ')
# write your code here!


def counter(sentence):
    count_letters = {}
    letters = sentence.replace(" ", "")
    for letter in letters:
        if letter not in count_letters:
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1
    return count_letters


print(counter(sentence))
