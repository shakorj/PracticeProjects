'''
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that
takes this list a and makes a new list that has only the even elements
of this list in it.

The idea of a list comprehension is to make code more compact to
accomplish tasks involving lists.
'''
def multi_line():
    list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = []

    for num in list:
        if num % 2 == 0:
            even_list.append(num)
    return print(even_list)

def single_line():
    list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = [num for num in list if num % 2 == 0] #list comprehension
    return print(even_list)

def main():
    multi_line()
    single_line()

if __name__ == '__main__':
    main()
