# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:05:03 2020

@author: athar
"""
from statistics import mean, median

# laps = int(input('How many laps have you run? '))
# for i in range(laps):
#     collect = []
#     colips = int(input('The time for the array is:'))
#     collect.append(colips)
#     for j in collect:
#         print(collect)

loop = int(input('Loops number'))

while loop != 0:
        collect =[]
        #time = int(input('Time for each loop?'))
        times = [20, 30, 40]
        for j in times:
            collect.append(j)
            summ =sum(collect)
            length = len(collect)
            average = summ /length

