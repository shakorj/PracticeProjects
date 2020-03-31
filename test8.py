play = True
while play:
    user1 = input("Rock-Paper-Scissors?: ")
    user2 = input("Rock-Paper-Scissors?: ")
    if user1 is "rock" and user2 is "scissors":
        print("User1 Wins")
        play = False
    elif user1 is "scissors" and user2 is "paper":
        print("User1 Wins")
        play = False
    elif user1 is "paper" and user2 is "rock":
        print("User1 Wins")
        play = False
    elif user1 == user2:
        print("It's a draw")
        play = False
    else:
        print("User2 Wins")
        play = False
