#Saving / writing to a file

def file_name():
    with open('new_file.txt', 'w') as open_file:
        open_file.write('This is a new file')
    return "Created a new file"

file = file_name()
print(file)

#Reading from a file
def read_file():
    with open('new_file.txt', 'r') as open_file:
        all_text = open_file.read()
    return all_text

read = read_file()
print(read)
