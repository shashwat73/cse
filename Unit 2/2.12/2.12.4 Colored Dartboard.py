speed()
radius = 100

def draw_circle():
    color_choice = input("What color should this circle be?: ")
    pendown()
    color(color_choice)
    begin_fill()
    circle(radius)
    penup()
    end_fill()
    left(90)
    forward(25)
    right(90)

penup()
setposition(0, -100)
for i in range(4):
        draw_circle()
        radius = radius - 25
