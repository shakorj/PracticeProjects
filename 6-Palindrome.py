'''
Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)

List Indexing: The first number is the “start index” and
the last number is the “end index.”
You can also include a third number in the indexing, to count how
often you should read from the list:
'''

def palindrome():
    user_input = input("Enter a word: ").lower()
    backward = user_input[::-1] #List indexing

    if user_input == backward:
        print("Palindrome")
    else:
        print("Not a Palindrome")


if __name__ == '__main__':
    palindrome()
