def sentence():
    a = input("Write a sentence: ")
    a = a.split()
    a = a[::-1]
    e = ' '.join(a)
    return (e)
a = sentence()
print(a)
#Taking a sentence and repeating it backwards to the user - using a function
