text = input("Enter some text: ")
y = text.lower()
x = text.split()
z = "owl"
c = 0
index = 0
index1 = []
for i in range(len(x)):
    if z in x[index]:
        c = c + 1
        index1.append(index)
    index = index + 1

print "There were " + str(c) + " words that contained \"owl\"."
print "They occurred at indices: " + str(index1)
