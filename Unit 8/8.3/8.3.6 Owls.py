text = input("Enter some text: ")
y = text.lower()
x = text.split()
z = "owl"
count = 0
index = 0
for i in range(len(x)):
    if z in x[index]:
        count = count + 1
    index = index + 1

print "There were " + str(count) + " words that contained \"owl\"."
