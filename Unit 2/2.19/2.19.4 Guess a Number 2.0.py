speed(0)
secret_number = 7

def draw_checkmark():
    clear()
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

def draw_up_arrow():
    clear()
    color("yellow")
    right(90)
    forward(100)
    backward(150)
    right(45)
    forward(50)
    backward(50)
    left(90)
    forward(50)
    backward(50)
    left(45)
    setposition(0,0)

def draw_down_arrow():
    clear()
    color("red")
    left(90)
    forward(100)
    backward(150)
    right(45)
    forward(50)
    backward(50)
    left(90)
    forward(50)
    backward(50)
    right(135)
    setposition(0,0)

user_number = int(input("Enter a numba: "))

while user_number != secret_number:
    if user_number > secret_number:
        draw_down_arrow()
        user_number = int(input("thas not da numba")
    else:
            draw_up_arrow()
            user_number = int(input(" thas not da number")
draw_checkmarck()
