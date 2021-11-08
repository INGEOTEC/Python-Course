# https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv

file = open("titanic.csv")
print(file)
file.close()

file = open("titanic.csv")
for line in file:
    line = line.strip()
    print(line)
file.close()

file = open("aaaa.csv")

file = open("titanic.csv")
for line in file.readlines():
    print(line)
file.close()

file = open("tmp.csv", "w")
file.close()


file = open("tmp.csv", "a")
# file.write('a,b,c', 'adsfas')
file.write('a,b,c\n')
file.close()


file = open("tmp.csv", "w")
print('a,b,c', 'adsfas', file=file)
# print('hi!', file=file)
# print('bye!', file=file)
file.close()

with open('titanic.csv') as file:
    lines = file.readlines()
    # file.close()

