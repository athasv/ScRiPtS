# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 02:27:48 2020

@author: athar
"""


# s1 = 'mark'
# s2 = 'mary'

# print('Length of s1 is: ', len(s1), 'and ', 'length of s2 is: ', len(s2))

# if s1 > s2:
#     print('bigger')
# else:
#     print('smaller')

# keep_going = 'y'
# # Calculate a series of commissions.
# while keep_going == 'y':
#     print('lets check while loop')
#     print('checked ')
#     keep_going = input('want to chek more? ')

print()
print('Number\t\tSquare\t\tResult')
print('=' * 70)
# for i in range(1, 20):
#     j = i * i
#     print(i, '\t', j)


def prints(value_1, value_2):
    return pow(value_1, value_2)


for i in range(0, 10):
    for j in range(0, 10):
        print(i, '\t*\t', j, '\t=\t', prints(i,j))
    print('=' * 70)
