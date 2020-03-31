import random
LL = 'abcdefghijklmnopqrstuvwxyz'
UL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Sym = '!@#$%^&*()'
password = input("Would you like a new password? ")
if password == "Yes" or password == "yes":
    #user = input("A strong or weak password? ")
    #if user == "strong":
        np = random.choice(UL)
        np2 = random.randint(0,100)
        np3 = random.sample(LL, 5)
        np4 = ''.join(np3)
        np5 = random.choice(Sym)
        print("New password: " + np + str(np2) + str(np4) + np5)
elif password == "No" or password == "no":
    print("Okay goodbye ")
#Password Generator first try (see R1 for updated code)
