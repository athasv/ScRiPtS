# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:53:02 2020

@author: athar
"""

import random

print('Welcome to the number guess game')
number_to_guess = random.randint(1,5)
count_number_of_tries = 1
guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
    print('Sorry wrong number')
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries , 'goes to complete the game')
else:
    print("Sorry - you loose")
    print('The number you needed to guess was', number_to_guess)
print('Game Over')
