number = input("Give me a number: ")
number = int(number)
Divisors = []
list = range(1, 101)
for x in list:
    cal = number % int(x)
    if cal <= int('0'):
        Divisors.append(x)
print("Divisors of your number " + str(Divisors))
