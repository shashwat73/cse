speed(0)
secret_number = 7

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

user_number = 7

user_number = int(input("Enter a number 1-10: "))

while user_number !=secret_number:
    user_number = int(input("That's not a number lol."))

draw_checkmark()
