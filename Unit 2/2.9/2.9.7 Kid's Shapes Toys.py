def set_position():
    penup()
    setpostion(-100,75)
    pendown()

#diamond
penup()
setposition(-100,75)
pendown()
begin_fill()
color("red")
circle(60,360,4)
end_fill()

#circle
penup()
setposition(100,75)
pendown()
begin_fill()
color("blue")
circle(60)
end_fill()

#pentagon
penup()
setposition(100,-75)
pendown()
begin_fill()
color("green")
circle(60,360,5)
end_fill()

#half circle
penup()
setposition(-100,-75)
pendown()
begin_fill()
color("yellow")
circle(60,180)
end_fill()
