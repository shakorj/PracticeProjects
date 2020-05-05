'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
'''

import random

def random_game():
    random_num = random.randint(1,10)

    while True:
        user_guess = input("Guess a number: ")

        if int(user_guess) == random_num:
            print("Exactly right")
            exit()
        elif int(user_guess) > random_num:
            print("Too high")
        else:
            print("Too low")
    return

if __name__ == '__main__':
    random_game()
