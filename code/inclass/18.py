def func(a):
    a[0] = 1
    a[1] = 2
    a[2].append(3)

lst = [None, None, list()]
func(lst[:])
print(lst)

b = list()
lst = ["M", 1, b[:]]
func(lst)
print(b)
print(lst)

a = []
print(a is [])
a = ""
print(a is "")

a = []
print(a is [])
a = ""
print(a is "")

lst = []
lst = list()

lst = list("abc")

lst = []
for i in "abc":
    lst.append(i)

lst = []
for i in "abc":
    lst.append(i*2)

lst = []
for i in "abc":
    if i != "b":
        lst.append(i*2)

lst = [i*2 for i in "abc" if i != "b"]


## CSV
cdn = "12,32,4\n42.2,-23.4,32"
cdn.split()

[x for x in cdn.split()]

[x.split(",") for x in cdn.split()]

[[float(i) for i in x.split(",")] for x in cdn.split()]








