# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:29:06 2020

@author: athar
"""


for i in range(6):
    for j in range(i):
        print('pop ', end='')
    print(' #pop')

# This program displays a stair–step pattern.
NUM_STEPS = 6
for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='')
    print('#')
