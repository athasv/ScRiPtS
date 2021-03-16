# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 02:13:13 2020

@author: athar
"""
def chech_if_user_has_finished():
    finishedl = True
    accepted = False
    while not accepted:
        useroperend = input('Another operation? ')
        if useroperend == 'y':
            accepted = True
        elif useroperend == 'n':
            finishedl = True
        else:
            print('Give y or n! ')
    return finishedl


finished = False
while not finished:
    result = 0
    user_oper = input("Which operation? ")
    
    print('Result: ', result)
    print("================")
    finished = chech_if_user_has_finished()
    
    
print('Bye')
def add(x, y):
"""" Adds two numbers """
    return x + y
def subtract(x, y):
""" Subtracts two numbers """
    return x - y
def multiply(x, y):
""" Multiples two numbers """
    return x * y
def divide(x, y):
"""Divides two numbers"""
    return x / y
