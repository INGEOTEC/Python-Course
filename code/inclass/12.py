import random

def func1(data):
    value = data[0]
    for var in data:
        if var < value:
            value = var
    return value


def func2(data):
    value = data[0]
    for var in data:
        if var > value:
            value = var
    return value


def func3(data):
    N = len(data)
    cnt = 0
    for var in data:
        cnt += var
    return cnt / N

def func4(data):
    m = func3(data)
    N = len(data)
    cnt = 0
    for var in data:
        cnt += (var - m)**2
    return cnt / (N - 1)


a = list(range(1, 10))
random.shuffle(a)

# print(func1(a))
# print(func2(a))
print(func3(a))
print(func4(a))



def den(i):
    cnt = 1
    for j in range(i, i+3):
        cnt = cnt * j
    return cnt


def factor(flag, i):
    if flag:
        return 4 / den(i)
    return - 4 / den(i)


import math
pi = 3
prev = 0
flag = True
i = 2
while math.fabs(pi - prev) > 1e-4:
    prev = pi
    pi += factor(flag, i)
    flag = not flag
    i += 2
    print(pi, math.fabs(pi - prev))
