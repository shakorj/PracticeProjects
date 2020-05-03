'''
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
 the first and last elements of the given list. For practice,
 write this code inside a function.
 '''
import random

def listends():
    randlist = random.sample(range(100),6)
    print(randlist)
    new_list = []
    new_list.append(randlist[0])
    new_list.append(randlist[-1])
    return print(new_list)

if __name__ == '__main__':
    listends()
