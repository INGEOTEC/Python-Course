for i in range(10): #Header
    i = i + 1 # Body
    print("i", i) # Body

# loop's header
for i in range(10): 
    # loop's body and if's header
    if i % 2 == 0: 
        # loop's body and if's body
        print(i, "is even")
    # loop's body and else's header 
    else: 
        # loop's body and else's body
        print(i, "is odd")

def square(x):
    return x*x

# create a function that add two numbers
def add(x, y):
    print("x", x)
    return x + y

print(square(2))
print(add(2, 3.1))


def header(name):
    total = 10
    length = len(name)
    print("*" * (total + length))
    print("*" * 5, end="")
    print(name, end="")
    print("*" * 5)
    print("*" * (total + length))

header("Mario")
