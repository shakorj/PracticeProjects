'''
For this exercise, we will keep track of when our friend’s birthdays are,
and be able to find that information based on their name. Create a dictionary
(in your file) of names and birthdays. When you run your program it should ask
the user to enter a name, and return the birthday of that person back to them.
'''

Birthdays = {"KOR": '10/1/2000', "ALLY": '12/1/2000'}
print("Welcome to the birthday dictionary! We know the birthdays of: ")
print(list(Birthdays.keys()))
user_input = input("Who's birthday do you want to look up?: ").upper()
if user_input in Birthdays:
    print(user_input + "'s birthday is " + Birthdays[user_input])
else:
    print("Name does not exist")
