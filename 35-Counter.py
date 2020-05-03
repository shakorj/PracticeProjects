from collections import Counter
# Counter takes a list and counts how many of each element were in the list.
fruits = ["apples", 'oranges', "apples", 'grapes', 'apples', 'oranges', 'grapes']
c = Counter(fruits)
print(c)
