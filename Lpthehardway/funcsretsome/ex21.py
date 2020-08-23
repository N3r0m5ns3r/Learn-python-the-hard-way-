def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def sub(a, b):
    print(f"subbing {a} - {b}")
    return a - b

def mul(a, b):
    print(f"mul {a} * {b}")
    return a * b

def div(a, b):
    print(f"div {a} / {b}")
    return a / b

print("Let's do some maths with just functions!")

age = add(30, 5)
height = sub(78, 4)
weight = mul(90, 2)
iq = div(900, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

print("Here is a puzzle.")

what = add(age, sub(height, mul(weight, div(iq, 2))))
print("That becomes: ", what," Can you do it by hand?")
