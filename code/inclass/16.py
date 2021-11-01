c = ["a", 21, ["z"]]
a = [12]

a in c + a
12 in c + a

-1 * [None, None] 
[1, 2] * 2

[12, 12] == [12] * 2

["z"] in c

d = ["z"]

d in c

del c[-1][0]
c

a = [1, 2, 3]
b = [1, 2, 3]

def reverse(lst):
    lst[:] = lst[::-1]

lst = [1, 2, 3]
reverse(lst)
lst

'a,b,c'.split(',')
'a,b,c'.split('b')

','.join(['v1', 'v2'])

lst = [['c', 1], ['a', 3], ['b', 2]]
lst.sort()
lst

def second(x):
    return x[1]

lst.sort(key=second)
lst