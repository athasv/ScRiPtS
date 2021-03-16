# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:51:24 2020

@author: athar
"""


def get_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('Invalid ')
        value_as_string = input(message)
        return int(value_as_string)


print(get_input(300))
print(get_input('loko'))
print(get_input(3000))