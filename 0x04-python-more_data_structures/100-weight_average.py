#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    list1 = []
    add1 = 0
    result = 0
    for i in my_list:
        list1.append(i[0] * i[1])

    for j in list1:
        add1 += j

    for k in my_list:
        result += k[1]

    result = add1 / result
    return result
