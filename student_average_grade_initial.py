# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:06:30 2020

@author: athar
"""
tot_stud = int(input('How many students? '))
tot_scor = int(input('How many scores  ? '))

for i in range(tot_stud):
    total = 0.0
    print('Data for student: ', i+1)
    for j in range(tot_scor):
        print('Total scores: ', j+1, end='')
        score = float(input(': '))
        total += score
    average = total/tot_scor
    print('The average score for student ', i+1, ' is: ', average)
    print()
