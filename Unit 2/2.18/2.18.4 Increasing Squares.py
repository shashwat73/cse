speed(0)
length = 50

while length < 400:
    penup()
    backward(length / 2)
    right(90)
    forward(length / 2)
    left(90)
    pendown()
    for i in range (4):
        forward(length)
        left(90)
    penup()
    forward(length / 2)
    left(90)
    forward(length /2)
    right(90)
    length = length + 50
