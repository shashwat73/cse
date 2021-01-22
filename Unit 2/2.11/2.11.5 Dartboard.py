"""
2.11.5 LINE of increasing bloicks
"""
speed()
length = 10

def draw_block():
    pendown()
    for i in range(4):
        forward(length)
        left(90)
    penup()
    forward(length*2)

penup()
setposition(-150,0)

for i in range(5):
    draw_block()
    length = length + 10
