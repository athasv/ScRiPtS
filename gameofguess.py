# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:48:42 2020

@author: athar
"""
#You could create another function that will implement the main game playing loop.
import random

num_guess = random.randint(1, 30)
input_guess = int(input("Gimme a number guess between 1 t0 30! "))
count_num_tries = 1
# if input_guess == num_guess:
#     print('You got the correct guess, ', num_guess)
# else:
#     if input_guess != num_guess:
#         if count_num_tries == 5:
#             break
#         if input_guess > num_guess:
#             print('We need a lower number')
#         else:
#             print('We need a higher number')
#             input_guess2 = int(input('Gimme a new number guess! '))
#             if input_guess2 > input_guess:
#                 print("Thats ok")
#             else:
#                 print('Lets start over!')
#                 count_of_tries += 1
if input_guess == num_guess:
    print('That the number: ', num_guess)
elif input_guess != num_guess:
    if input_guess > num_guess:
        print('We need a lower number')
    elif print('We need a higher number'):
        input_guess2 = int(input('Gimme a new number guess! '))
        if input_guess2 > input_guess:
            print('Thats ok')
        else:
            print('Lets start over!')
            count_num_tries +=1
    else:
        print('What a mess!')
else:
    print('Nothing worked!')
