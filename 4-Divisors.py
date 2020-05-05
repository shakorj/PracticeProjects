'''
Create a program that asks the user for a number and
then prints out a list of all the divisors of that number.
'''

def answer(divisors_list):
    list_length = len(divisors_list)
    if list_length == 0:
        print("Error - Prime Number")
    else:
        print(divisors_list)

def divisors():
    number = input("Enter a number: ")
    divisors_list = []
    population_range = range(2, int(number))
    for x in population_range:
        if int(number) % x == 0:
            divisors_list.append(x)
    answer(divisors_list)

if __name__ == '__main__':
    divisors()
