# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 02:14:40 2020

@author: athar
"""


def input_data(price, discount):
    """..."""
    multiplier_1 = 0.1
    multiplier_2 = 0.01
    total_price = 0.0
    if len(str(discount)) == 1:
        discount = discount * multiplier_1
    else:
        if len(str(discount)) == 2:
            discount = discount * multiplier_2
    total_price = discount * price
    print('The total price is: ', total_price)
    print('=' * 40)


print('=' * 40)
input_price = int(input('How much is the price? '))
print('=' * 40)
input_disco = int(input('How much is the discount? '))
print('=' * 40)
item = input_data(input_price, input_disco)
print(item)
