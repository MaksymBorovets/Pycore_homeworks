x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

def compare(x, y):
    """This function returns the largest of two numbers"""
    if x > y: print(f"{x} is greater than {y}")
    elif x == y: print(f"{x} and {y} are equal")
    else: print(f"{y} is greater than {x}")
    return compare
compare(x, y)