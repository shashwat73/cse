list_num = []
for i in range(5):
    num = int(input("Number: "))
    list_num.append(num)
    print list_num

index = 0
total = 0
for i in range(5):
    total = int(total) + int(list_num[index])
    index = index + 1

print "Sum: " + str(total)
