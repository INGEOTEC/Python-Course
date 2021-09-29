def add(a, b):
    """Add two numbers
    >>> add(12, 2.1)
    14.1
    """

    for x in [a, b]:
        f = isinstance(x, float)
        f = f or isinstance(x, int)
        assert f
    return a + b

def is_even(a):
    # a = 12
    """Is even?
    >>> is_even(12)
    True
    """

    return a % 2 == 0