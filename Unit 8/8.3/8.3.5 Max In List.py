my_list = [5, 2, -5, 10, 23, -21]

def max_int_in_list(x):
    max_num = 0
    for i in range(len(x)):
        if x[i] > max_num:
            max_num = x[i]
    return max_num

print max_int_in_list([5, 2, -5, 10, 23, -21])
