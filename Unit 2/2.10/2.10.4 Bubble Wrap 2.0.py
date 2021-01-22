"""
Sum cool stuff
"""
speed(0)
# cool stuff
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)

# This function will draw one row of 10 circles
def draw_circle_row():
    for i in range(10):
        color("lightblue")
        begin_fill()
        circle(20)
        end_fill()
        penup()
        forward(10)
        left(90)
        forward(20)
        pendown()
        color("white")
        circle(10, 90)
        penup()
        left(90)
        forward(30)
        left(90)
        forward(40)


# Send Tracy to starting position in bottom left corner
penup()
setposition(-180,-200)
# Call circle drawing function 10 times to fill ten rows
for i in range(10):
    draw_circle_row()
    move_up_a_row()
