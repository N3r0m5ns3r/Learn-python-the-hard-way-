# importing argv from sys
from sys import argv
# args
script, input_file = argv
# defining functions
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# opening inputted file
current_file = open(input_file)

print("first let's print the whole file:\n")

#prints
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:\n")

# adding new line
current_line = 1
print_a_line(current_line, current_file)
# adding new line
current_line = current_line + 1
print_a_line(current_line, current_file)
# same ^
current_line = current_line + 1
print_a_line(current_line, current_file)
