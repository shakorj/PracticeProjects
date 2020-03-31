#Determining if a number is prime or not using modulo operator
def get_integer():
    return int(input("Give me a number: "))
Divisors = []
number = get_integer()
list = range(1, number+1)
for x in list:
    cal = number % int(x)
    if cal <= int('0'):
        Divisors.append(x)
#print(" " + str(Divisors))
#print(len(Divisors))
#print(Divisors.count(int(x))) - this was wrong
if len(Divisors) <= int('2'):
    print("Your number is a prime number")
else:
    print("Your number is a not prime number")
