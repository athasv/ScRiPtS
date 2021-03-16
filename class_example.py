# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 01:19:39 2020

@author: athar
"""
# this program gets items original price
# calculates sale price with 20% discount


class Shape_data:

    def __init__(self, price, discount, total_price):
        self.__price = price
        self.__discount = discount
        self.__total_price = total_price

    def set_price(self, price):
        self.__price = price

    def set_total_price(self, total_price):
        self._total_price = price * discount

    def set_discount(self, discount):
        self.__discount = self.__discount * 0.1

    def get_price(self):
        return self.__price

    def get_discount(self):
        return self.__discount

    def get_total_price(self):
        return self.__total_price


def item_data():
    input_price = input("How much does it cost? ")
    input_discount = input('How much is the discount? ')
    input_total_price = Shape_data.get_total_price(self)
    item = Shape_data(input_price, input_discount, input_total_price)
    print('The price is: ', item.get_price())
    print('The discount is : ', item.get_discount())
    print('The total price is: ', item.get_total_price())


item_data()
