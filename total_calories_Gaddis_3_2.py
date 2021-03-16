# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:00:48 2020

@author: athar
"""

cal_per_min = 4.2
min_intervals =[10, 15, 20, 25, 30]

for i in min_intervals:
    total_cal = 0
    total_cal = i * cal_per_min
    print('For interval of minutes', i, 'the calories burnt are: ', total_cal)
