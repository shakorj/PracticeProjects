'''
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a
list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for
that in a different function.
'''

def duplicates():
  list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  new_list = set(list)
  return print(new_list)

if __name__ == '__main__':
    duplicates()
