new = "!"
string = input("Enter text: ")
x = list(string)
index = 0
for i in range(len(string)):
    if x[index] == "i":
        x[index] = new
    index = index + 1

print"".join(x)
