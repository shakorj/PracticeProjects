number = input("Please enter a number: ")
number = int(number)
cal = number % int('2')
if cal > int('0'):
    print("You picked a odd number")
else:
    print("You picked a even number")
