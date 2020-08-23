#!/usr/bin/env python3

# importing argv from sys lib
from sys import argv

# args
script, filename = argv

# choosing the arg and erasing the chosen file adding a ret comand
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
# opening the file
print("Opening the file ...")
target = open(filename, 'w')

# truncanting the file this will delete all data in the file
print("Truncating the file. Goodbye!")
target.truncate()

# input what u want
print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3; ")

# writing to the file
print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# closing the file

target.close()
