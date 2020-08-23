def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: arg{2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print(" Got nuffin dude.")


print_two("zeus", "god")
print_two_again("zeus", "god")
print_one("!first")
print_none()
