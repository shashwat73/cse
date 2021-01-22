speed(0)

def make_square(i):
    if i % 2 == 0:
        begin_fill()
    for i in range(4):
        forward(25)
        left(90)
    end_fill()

penup()
setposition(-100, 0)
pendown()
for i in range (6):
    pendown()
    make_square(i)
    penup()
    forward(35)
