'''
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list
that are less than 5.

Extras:
Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.

Ask the user for a number and return a list that contains only elements
from the original list a that are smaller than that number given by the user.
'''
#-----------------------------------------------------------------------------
List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
New_List = []

for x in List:
    if x <= 5:
        New_List.append(x)
print(New_List)


#----------------------------------------------------------------------------
user_input = input("Pick a number: ")
Small_List = []

for x in List:
    if int(user_input) >= x:
        Small_List.append(x)
print(Small_List)
