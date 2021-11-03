lines = ["12,-34.2 , 23", "-2, 34, 43.2"]

# first step
for line in lines:
    lst = line.split(",")
    print(lst)



# Second step
for line in lines:
    lst = line.split(",")
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    print(lst)

# Third step
output = []
for line in lines:
    lst = line.split(",")
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    output.append(lst)

# Transform to a function
def csv_matrix(data):
    output = []
    for line in data:
        lst = line.split(",")
        for i in range(len(lst)):
            lst[i] = float(lst[i])
        output.append(lst)
    return output
print(csv_matrix(lines))

# Without return
def csv_matrix2(data, output):
    for line in data:
        lst = line.split(",")
        for i in range(len(lst)):
            lst[i] = float(lst[i])
        output.append(lst)
oo2 = []
print(csv_matrix2(lines, oo2))
print(oo2)

if True:
    oo3 = []
    csv_matrix2(lines, oo3[:])
    print(oo3)

