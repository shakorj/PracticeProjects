#Using the While function to guess a number 
import random
a = random.randint(1,9)
count = 0
while True:
    user = input("Guess a number between 1 & 9: ")
    if user == "exit":
        break
    else:
        user = int(user)
        count += 1
        if user > a:
            print("You guessed too high")
        elif user < a:
            print("You guessed too low")
        else:
            print("Exactly Right")
            print("It took you only", count, "tries")
