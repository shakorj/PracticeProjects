import random
num = str(random.randrange(1, 9999, 4))
user = input("Guess a 4-digit number: ")
#num2 = [int(x) for x in str(num)]
#user2 = [int(x) for x in str(user)]
#print compare(num2, user2)
print(num)
#print(user2)
cowbull = [0,0]
#cows = user guessed correctly in the correct place
#bull = user guessed correctly in the wrong place
for x in range(len(num)):
    if num[x] == user[x]:
        cowbull[1]+=1
    elif num[x] in user[x]:
        cowbull[0]+=1
print(cowbull)
