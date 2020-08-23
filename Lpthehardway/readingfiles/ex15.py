#!/usr/bin/env python3 

# importing argv from sys
from sys import argv

# args
script, filename = argv

# opening the filename arg
txt = open(filename)

# printing and reading the file arg
print(f"here's your file {filename}:")
print(txt.read())

# reprinting and re reading the file arg
print("Type the filename again:")
file_again = input('> ')
txt_again = open(file_again)

print(txt_again.read())


txt.close() 
txt_again.close() 


