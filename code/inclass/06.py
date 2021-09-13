# [0, 1, 2, 3, ..., 10]
y = 0
for i in range(1, 11):
    y = y + i
print("sum: ", y)

print(range(2, 10, 2))
# range(2, 10, 2)

y = 0
for i in range(0, 10):
    print("y", y, "i", i)
    y = y + 1 / 2 ** i
print(y)
# 1.998046875

import turtle
juan = turtle.Turtle()

juan.forward(100)
juan.left(90)
juan.forward(100)
juan.left(90)
juan.forward(100)
juan.left(90)
juan.forward(100)
juan.left(90)

for i in range(4):
    print(i)
    juan.forward(100)
    juan.left(90)


for var in [1, "mario", 23.3, "blue"]:
    print("type:", type(var), "value:", var)


import turtle
juan = turtle.Turtle()

for action in ["left", "left", "left", "left", 
               "blue",
               "right", "right", "right"]:   
    if action == "left":
        juan.left(90)
        # juan.forward(100)        
    elif action == "right":
        juan.right(90)
        # juan.forward(100)        
    else:
        juan.color(action)
    if action == "left" or action == "right":
        juan.forward(100)
