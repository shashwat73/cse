speed(0)
square_length = int(input("Enter size of square: "))

def draw_square():
    for i in range (4):
        forward(square_length)
        right(90)

penup()
setposition(-200,200)
pendown()
draw_square()

penup()
setposition(200-square_length,200)
pendown()
draw_square()

penup()
setposition(-200,-200+square_length)
pendown()
draw_square()

penup()
setposition(200-square_length,-200+square_length)
pendown()
draw_square()
