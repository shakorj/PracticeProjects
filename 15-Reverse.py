'''
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except
with the words in backwards order.
'''
def reverse():
  user_input = input("Write a sentence: ")
  split_words = user_input.split()
  reverse = split_words[::-1]
  answer = ' '.join(reverse)
  return print(answer)

if __name__ == '__main__':
    reverse()
