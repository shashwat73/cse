# Set row value to 0
speed(0)
penup()
row_value=0
radius = 25

# This function moves to next row with x-value based on how many blocks are to
# be placed and the y-value based on the row number (gets 50 pixels higher each row)
def move_to_row(num_blocks):
    x_value = -((num_blocks*50)/2) + radius
    y_value = -200+(50*row_value)
    setposition(x_value,y_value)

# This function draw a row of blocks based on user value
def draw_block_row(num_blocks):
    for i in range(num_blocks):
        pendown()
        circle(radius)
        penup()
        forward(50)

# Ask the user how many blocks should be on bottom row
num_blocks=int(input("How many blocks on the bottom row? (8 or less): "))

# Call function to move Tracy to beginning of row position and then increase row
# variable value. Then Tracy will draw the row of blocks needed and subtract one
# from the num blocks variable.
for i in range(num_blocks):
    move_to_row(num_blocks)
    row_value=row_value+1
    draw_block_row(num_blocks)
    num_blocks=num_blocks-1
