import math

# add two numbers

frst = input("First number: ")
scnd = input("Second number: ")

result = frst + scnd
print("The result is: ", result)

frst = input("First number: ")
scnd = input("Second number: ")
print("frst: ", type(frst), frst)
print("scnd: ", type(scnd), scnd)
result = frst + scnd
print("The result is: ", result)
# frst:  <class 'str'> 2
# scnd:  <class 'str'> 4
# The result is:  24

frst = float(input("First number: "))
scnd = float(input("Second number: "))
print("frst: ", type(frst), frst)
print("scnd: ", type(scnd), scnd)
result = frst + scnd
print("The result is: ", result)
# frst:  <class 'float'> 2.0
# scnd:  <class 'float'> 4.0
# The result is:  6.0

#_ = input("First number: ")
frst = float("2") # _) # Input!!
#_ = input("First number: ")
scnd = float("4") # _) # Input!!
result = frst + scnd
print("The result is: ", result)
# The result is:  6.0

print("12" + 3)

# Transform degrees to radians

degrees = 15
radians = degrees * math.pi / 180
print("radians: ", radians)

degrees = -15
if degrees > 0:
    radians = degrees * math.pi / 180
else:
    radians = (360 + degrees) * math.pi / 180
print("radians: ", radians)
# radians:  6.021385919380437

degrees = -15
if degrees < 0:
    print("negative", degrees)
    0 / 0
    degrees = (360 + degrees)
radians = degrees * math.pi / 180    
print("radians: ", radians)
# radians:  6.021385919380437

degrees = -(15 + 360)
if degrees < 0:
    if degrees < -360:
        degrees = -(math.fabs(degrees) % 360)
    degrees = (360 + degrees) % 360
degrees = degrees % 360
radians = degrees * math.pi / 180    
print("radians: ", radians)
# radians: 6.021385919380437

op = input("Which operation do you want to do: ")
if op == '+':
    res = arg1 + arg2
else: 
    if op == '-':
        res = arg1 - arg2
    else:
        if op == '/':
            res = arg1 / arg2
        else:
            # *
            res = "NaN"
            print("Operation not found") 
print("Result: ", res)


op = input("Which operation do you want to do: ")
arg1 = float(input("op1: "))
arg2 = float(input("op2: "))
if op == '+':
    res = arg1 + arg2
elif op == '-':
    res = arg1 - arg2
elif op == "/":
    res = arg1 / arg2
else:
    res = "NaN"
    print("Operation not found")    
print("Result: ", res)


frst = input("First number: ")
scnd = input("Second number: ")
if isinstance(frst, str):
    frst = float(frst)
if isinstance(scnd, str):
    scnd = float(scnd)
result = frst + scnd
print("The result is: ", result)
# frst:  <class 'str'> 2
# scnd:  <class 'str'> 4
# The result is:  24

# frst = input("First number: ")
frst = 13.3 # Change! only for test
# scnd = input("Second number: ")
scnd = 21.3 # Change! only for test
if isinstance(frst, str):
    frst = float(frst)
if isinstance(scnd, str):
    scnd = float(scnd)
result = frst + scnd
print("The result is: ", result)