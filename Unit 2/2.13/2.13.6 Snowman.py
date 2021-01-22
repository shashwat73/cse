inputs = [100]

speed(0)

def draw_circle(radius):
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(radius*2)
    right(90)

penup()
setposition(0, -200)
color("gray")

bottom_radius = int(input("What should the bottom circle's size be? "))

draw_circle(bottom_radius)
draw_circle(bottom_radius/2)
draw_circle(bottom_radius/4)
