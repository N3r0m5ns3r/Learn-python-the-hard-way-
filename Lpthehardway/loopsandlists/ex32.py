the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this is the first kind of for-loop goes trought a list

for number in the_count:
    print(f"this is count {number}")

# same as above

for fruit in fruits:
    print(f"a fruit of type: {fruit}")

# also we can go throught a mixed lists too

for i in change:
    print(f"I got {i}")


# we can also builf lists, first start with an empty one

elements = range(0, 6)

# then use the range function to do 0 to 5 counts

#for i in range(0, 6):
#    print(f"adding {i} to the list")
    # append is a fucntion that lists understand it will append to the empty we created 'elements'
#    elements.append(i)


# now we can print them out

for i in elements:
    print(f"element was: {i}")
