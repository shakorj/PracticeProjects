import string
import random
password = input("Would you like a new password? ")
if password == "No" or password == "no":
    print("Okay goodbye ")
    exit()
elif password == "Yes" or password == "yes":
    def password():
        pl = int(input("How many characters in your password? "))
        if pl <= 5:
            return "All passwords must be longer than 5 characters "
        else:
            char = string.ascii_letters
            dig = string.digits
            sym = string.punctuation
        return ''.join(random.sample(char, pl - 2)) + random.choice(dig) + random.choice(sym)
pw = password()
print("New password: " + pw)
#Password Generator using functions and string library
