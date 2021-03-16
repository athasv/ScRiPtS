# import random


def guess_game():   
    tempNum = 30
    count_tries = 1
    inputNum = int(input("Give me a number from 1 to 100: "))
    while inputNum != tempNum:
        if count_tries == 4:
            break
        elif inputNum > tempNum:
            print("too high!")
        else:
            print("too low!")
        inputNum = int(input("Please insert a new number: "))
        count_tries += 1
    if inputNum == tempNum:
        print("just right!")
    else:
        print("Sorry, try again from scratch!")
    print("End of the game! ")


example = guess_game()
