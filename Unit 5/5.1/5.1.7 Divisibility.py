numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).

while denominator == 0:
    denominator = int(input("Enter denominator: "))

if numerator / denominator * denominator == numerator:
    print "Divides evenly!"
else:
    print "Doesn't divide evenly."
