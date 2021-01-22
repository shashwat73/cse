inputs = (100)

speed(0)

def draw_red_square(side_length):
    color("red")
    begin_fill()
    for i in range(4):
        forward(side_length)
        left(90)
    end_fill()

def draw_blue_square(radius):
    color("blue")
    begin_fill()
    circle(radius)
    end_fill()

radius = int(input("What is the radius of the circle?: "))

penup()
right(90)
forward(radius)
left(90)
backward(radius)
pendown()
draw_red_square(radius*2)

forward(radius)
draw_blue_square(radius)
