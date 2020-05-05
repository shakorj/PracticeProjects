
def prime_list():
  #Writing a string to a text file - text file is write only
  with open('prime_list.txt', 'w') as open_file:
      population_range = range(2, 1001)
      population_list = []
      prime_numbers = []
      #Putting range of numbers into a List
      for x in population_range:
          population_list.append(x)

      #Identifying numbers that are divisible by a number other than 1 and itself
      for x in population_list:
          if x > 1:
            for n in range(2, x):
                if (x % n) == 0:
                    break
            #Creating a list of numbers that is not divisible  by anything
            else:
              prime_numbers.append(x)

      #Adding list of prime numbers to text file created above
      for number in prime_numbers:
          line = str(number) + '\n'
          open_file.write(line)

      return "Prime List Created"

prime_file = prime_list()
#print(prime_file)
#-----------------------------------------------------------------------------
def happy_number_list():
    happy_numbers_range = range(13, 15)
    happy_list = []
    happy_numbers = []
    n = 0

    for x in happy_numbers_range:
        happy_list.append(x)

    for number in happy_list:
        a = number % 10
        b = a**2
        #c = b + a
        print(b)
        for elem in str(number):
            c = int(elem)**2
            d = c + b
            print(d)
    return

a = happy_number_list()
print(a)
    #     if n in happy_numbers:
    #         return False
    #     happy_numbers.append(n)


        #return True

# with open('happy_list.txt', 'w') as open_file:
#     b = [x for x in range(1000) if happy_number_list(x)]
#     a = str(b)
#     open_file.write(a)
#print("Happy List Created")
#------------------------------------------------------------------------------
# def compare():
#         happy_list = []
#         i = 0
#         with open('happy_list.txt', "r") as open_file:
#             happy_text = open_file.readline()
#             while happy_text:
#                 print(i)
#                 i += 1
#                 happy_list.append(happy_text)
#                 #happy_list = str(happy_list).replace('[','').replace(']','')
#                 happy_text = open_file.readline()
#             #print(happy_list)
#
#         prime_list = []
#         with open('prime_list.txt', "r") as open_file:
#             prime_text = open_file.read()
#             while prime_text:
#                 prime_list.append(prime_text)
#                 #prime_list = str(prime_list).replace('[','').replace(']','')
#                 prime_text = open_file.read()
#             #print(prime_list)
#
#         Overlap_list = []
#         for number in happy_list:
#             if number in prime_list:
#                 Overlap_list.append(number)
#                 #Overlap_list = Overlap_list.replace('\n')
#             #print(Overlap_list)
#         return
#
# comparing = compare()
# #print(comparing)
