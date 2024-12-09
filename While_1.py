my_list = [42, 69, 322, 13, 0, 99, 5, 0, 8, -7, 6, 5]
i = 0
a = len(my_list)
while a > i:
    b = int(my_list[i])
    if b > 0:
        print(b)
        i = i + 1
    else:
        if b == 0:
            i = i + 1
        else:break