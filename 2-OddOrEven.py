'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an
even / odd number react differently when divided by 2?
'''

user_input = input("Enter a number: ")

if int(user_input) % 2:
  print("This number is odd")
else:
  print("This number is even")
