'''
write a function that picks a random word
from a list of words from the SOWPODS dictionary.
'''
import random
#-----------------------------------------------------------------------

def one_random_word(name):
    with open(name, 'r') as words:
        line = words.readlines()
    random_word = random.choice(line)
    return random_word

#------------------------------------------------------------------------

def generate_multiple_words(name, random_sample):
    list_of_words = []

    with open(name, 'r') as words:
        line = words.readlines()
        for word in line:
            word = word.strip()
            list_of_words.append(word)
    random_list = random.sample(list_of_words, random_sample)
    return random_list

#---------------------------------------------------------------------

random_list = 'sowpods.txt'
random_sample = 3

a = generate_multiple_words('sowpods.txt', random_sample)
b = one_random_word('sowpods.txt')
print(a)
