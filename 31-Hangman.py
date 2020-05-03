'''
Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter. The player guesses
one letter at a time until the entire word has been guessed.
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
the clue word that were guessed correctly.
'''
#--------------------------------------------------------------------
Hangman_word = 'MONEY'
length_of_word = len(Hangman_word)
User_Hint = "Another word for currency"
word_display = "_" * length_of_word #added based on looking at solution

user_word = ""
guessed_letters = [] #added based on looking at solution

user_guesses = 0
limit_guesses = 2
out_of_guesses = False

print("Welcome to Hangman!")
print("Here's your hint: " + User_Hint)
print('\n')
print(word_display)

#print("It took you " + str(user_guesses) + " guesses")

#--------------------------------------------------------------------
while user_word != Hangman_word:
    if user_guesses < limit_guesses:
        user_input = input("Guess a letter: ").upper()
        if user_input in Hangman_word:
            guessed_letters.append(user_input) #added based on looking at solution

            word_as_list = list(Hangman_word) #added based on looking at solution
            index = word_as_list.index(user_input)
            print(index)
            word_display[index] = user_input
            user_word = "".join(word_display)

            # find = Hangman_word.find(user_input)
            # letter = Hangman_word[int(find)]
            print(user_word)
        else:
            user_guesses += 1
            print("Incorrect!")
    else:
        out_of_guesses = True
        break
if out_of_guesses:
    print("You ran out of guesses. Game over!")

# if user_input == 'exit':
#     exit()
