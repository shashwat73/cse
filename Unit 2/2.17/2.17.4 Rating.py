speed(0)

def draw_checkmark():
    penup()
    backward(50)
    right(90)
    pendown()
    pensize(10)
    color("green")
    left(45)
    forward(50)
    left(90)
    forward(100)
    penup()

def draw_x():
    color("red")
    left(45)
    pensize(10)
    pendown()
    for i in range(4):
        forward(50)
        backward(50)
        left(90)

def draw_line():
    color("yellow")
    pensize(10)
    forward(50)
    backward(100)
    forward(50)

rating = int(input("What is your rating? (1-10)"))

if rating <= 4:
    draw_x()
elif rating >= 8:
    draw_checkmark()
else:
    draw_line()
