import random
# function to search if given number is in the list of numbers

def number_search():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    given_number = random.randrange(20)

    if given_number in numbers_list:
        print ("Your number is " + str(given_number) + " and it is in the list")
    else:
        print ("Your number is " + str(given_number) + " and it is not the list")
    return ("Search over")

answer = number_search()
print(answer)

#------------------------------------------------------------------------
#def numbers_list():
#    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    return numbers_list

#def given_number():
#    given_number = 4.5
#    return given_number

# def binary_search(numbers_list, given_number):
#     first = 0
#     last = len(numbers_list) - 1
#
#     while first <= last:
#         middle_of_list = (first + last) // 2
#
#         if numbers_list[middle_of_list] == given_number:
#             return given_number
#
#         elif numbers_list[middle_of_list] > given_number:
#             last = middle_of_list - 1
#         else:
#             first = middle_of_list + 1
#             return print("Number not found")
#
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search(numbers_list, 7))
