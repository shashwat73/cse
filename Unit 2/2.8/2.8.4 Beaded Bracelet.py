speed(0)

def make_bead():
    forward(100)
    pendown()
    circle(10)
    penup()
    backward(100)

penup()
for i in range(36):
    make_bead()
    left(10)
