list = [1, 2, 2, 3, 4, 5, 5, 5, 6]


def uni_num(list):
    list2 = []
    for number in list:
        if number in list2:
            continue
        else:
            list2.append(number)
    return list2

print(uni_num(list))