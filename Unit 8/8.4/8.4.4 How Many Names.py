num = int(input("Number of names: "))
full_name = ""

for i in range(num):
    name = input("Name: ")
    full_name = full_name + name + " "

full_name = full_name.split()
print "First name: " + str(full_name[0])
print "Middle name(s): " + str(full_name[1:num-1])
print "Last name: " + str(full_name[num-1])
