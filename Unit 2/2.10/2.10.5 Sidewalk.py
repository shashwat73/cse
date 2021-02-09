speed(0)
penup()
setposition(-200,-200)

def square():

    for i in range(8):
        pendown()
        right(45)
        circle(35,360,4)
        left(45)
        forward(50)
        penup()
setposition(-200,-200)

for i in range(4):
    square()
    left(90)
