"""
This code will draw hash marks at 25, 50, 100, and 200 pixels.
"""

speed()
radius = 25

def move_down():
    penup()
    right(90)
    forward(25)
    left(90)
    pendown()

for i in range(4):
    move_down()
    circle(radius)
    radius = radius + 25
