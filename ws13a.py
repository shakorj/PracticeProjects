import random
num = int(input("Enter the number of Fibonnaci numbers: "))
b = random.randint(0,1000)
a = [b,b]
for x in range(num - 2):
    a.append(a[-1] + a[-2])
print(a)
#Creating Fibonnaci numbers beginning at a random number
