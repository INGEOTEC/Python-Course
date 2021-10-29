def div(num, den):
    return num / den
    
def div(num=0, den=0):
    return num / den

def sum(*args):
    res = 0
    for x in args:
        res += x
    return res


def print_reverse(cdn):
    r = cdn[::-1]
    print(r)

def quotient_modulo(a, b):
    return a // b, a % b

a = quotient_modulo(13, 6)
print(a)
print("Value1", a[0])
print("Value2", a[1])
print(type(a))


def func(a, b, op=None):
    assert op is not None
    return op(a, b)

func(12, 2, op=sum)
func(12, 2, op=div)


def parabola(a, b, c):
    def func(x):
        return a * x * x + b * x + c
    return func

a = parabola(3, -1.2, 4)

def sum_lists(a, b):
    assert len(a) == len(b)
    cnt = 0
    output = 0
    for i in a:
        output += i + b[cnt]
        cnt += 1
    return output
res = sum_lists([3, 2, 1], [1, 2, 3])

def sum_lists(a, b):
    assert len(a) == len(b)
    output = 0
    for cnt, i in enumerate(a):
        output += i + b[cnt]
    return output


def sum_lists(a, b):
    output = 0
    for v1, v2 in zip(a, b):
        output += v1 + v2
    return output
res = sum_lists([3, 2, 1], [1, 2, 3])    
res2 = sum_lists([3, 2, 1], [1, 2])


def fib(x):
    assert x >= 0
    if x <= 1:
        return x 
    return fib(x-1) + fib(x-2)