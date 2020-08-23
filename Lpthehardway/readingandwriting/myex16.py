from sys import argv

scipt, filename = argv


print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
# opening the file
print("Opening the file ...")
target = open(filename, 'w')


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
