a = input("Give me a word: ")
mid = int(len(a)/2)
if mid % 2 is 0:
    b = a[-1:mid-1:-1]
else:
    b = a[-1:mid:-1]
c = a[:mid]
if b == c:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
