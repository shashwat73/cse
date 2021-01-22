speed (100)
pensize(5)
penup()
setposition(-100,0)
for i in range (4):
    #drawing the first side
    pendown()
    color("red")
    forward(50)

#2nd
left(120)
color("blue")
forward(50)

#3rd
left(120)
color("green")
forward(50)

#turnin around
penup()
left(120)
forward(50)
