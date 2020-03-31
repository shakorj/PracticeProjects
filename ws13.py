import random
def Fibonnaci():
    return int(input("Enter the number of Fibonnaci numbers: "))
a = Fibonnaci()
b = random.sample(range(100),a)
c = []
print(b)
for x in b:
    c.append(a - 1)
#b.append(a)
#b.append(a + a - 1)
#print(b)
