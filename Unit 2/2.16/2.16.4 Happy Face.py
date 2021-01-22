def draw_eye():
    penup()
    right(90)
    forward(10)
    left(90)
    begin_fill()
    color("black")
    circle(10)
    end_fill()

def draw_happy_mouth():
    setposition(-70,0)
    right(90)
    pensize(10)
    pendown()
    circle(70,100)

def draw_sad_mouth():
    setposition(50,-50)
    left(90)
    pensize(10)
    pendown()
    circle(50, 180)

def draw_smiley_face():
    penup()
    right(90)
    forward(100)
    left(90)
    begin_fill()
    color("yellow")
    circle(100)
    end_fill()
    setposition(-30,40)
    draw_eye();
    setposition(30,40)
    draw_eye();

happy = input("How you feel today")

draw_smiley_face()

if (happy == "1"):
    draw_happy_mouth()

else:
    draw_sad_mouth()
