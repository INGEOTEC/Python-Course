txt = "morning:good"
a = txt.split(":")
b = a[::-1]
print(b)

index = txt.index(":")
a = txt[:index]
b = txt[index+1:]
b = [b, a]
print(b)

try:
    fname = "nofile.txt"
    fpt = open(fname)
    data = fpt.readlines()
    fpt.close()
except FileNotFoundError as e:
    print("File not found", fname, e)


try:
    fname = 'hello.c'
    data = open(fname)
    if data.read():
        raise Exception
    # open for writing
except FileNotFoundError:
    print("File not found", fname)

try:
    fname = 'tmp.txt'
    fpt = open(fname, 'w')
    lines = fpt.readlines()
    fpt.close()
except FileNotFoundError:
    pass

a = [1, 2, "!"]
b = a
b[1] = "A"
print(a)

a = [1, 2, "!"]
b = a[:]
b[1] = "A"
print(a)
    