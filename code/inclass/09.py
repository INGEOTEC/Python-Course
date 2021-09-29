a = 2 // 3
print(type(a))
assert type(a) != int
assert isinstance(a, int)

def add(a, b):
    """Add two numbers"""
    return a + b

add(12, "23")


def add(a, b):
    for x in [a, b]:
        f = isinstance(x, float)
        f = f or isinstance(x, int)
        assert f
    return a + b

add("12", 3)

assert add(21, 1.2) == 22.2


def even_numbers(n):
    for i in range(n + 1):
        if is_even(i):
            print("Even", i)

def is_even(a):
    return a % 2 == 0


even_numbers(11)

def add(a, b):
    """Add two numbers"""
    for x in [a, b]:
        f = isinstance(x, float)
        f = f or isinstance(x, int)
        assert f
    return a + b


def gcd(a, b):
    """Greatest Common Divisor"""
    assert isinstance(a, int)
    assert isinstance(b, int)

gcd(12.2, 23)