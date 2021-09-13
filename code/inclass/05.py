# import math
# print(math)
# # <module 'math' ... >
# 
# math.pi
# # 3.141
# math.e
# # 2.718
# 
# math.sin(math.pi)
# # 1.2246467991473532e-16
# math.cos(math.pi)
# # -1.0
# math.log(1024)
# # 6.931471805599453
# 
# import random
# random.random()
# # 0.6659832639132849
# random.random()
# # 0.5013513891044694
# 
# random.randint(-2, 4)
# # -1

import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# Create the agent
juan = turtle.Turtle()
# Give instructions 
# dot notation
juan.forward(150)
juan.left(90)    
juan.forward(75)
# 
juan.color("red")
juan.left(90)
juan.forward(70)

pepe = turtle.Turtle()
pepe.color("blue")
pepe.right(180)
pepe.forward(60)

# losing juan and replacing it
# juan = pepe
# juan.left(45)
# juan.forward(100)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
juan.clear()
wn.exitonclick()

# 
# 
# juan.clear()
# 

