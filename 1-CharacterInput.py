'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.
'''

user_input_name = input("Enter your name: ")
user_input_age = input("Enter your age: ")

year = (100 - int(user_input_age)) + 2020
print(user_input_name + " you will turn 100yrs old in " + str(year))
