
my_list = []
for i in range(5):
  name = input("Name: ")
  x = name.split()
  my_list.append(x[(len(x)-1)])

my_list.sort()
print my_list
