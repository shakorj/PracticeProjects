a = [5, 10, 15, 20, 25]
b = []
b.append(a[:1] + a[-1:])
print(b)
#printing a new list of the first and last elements in a given list
