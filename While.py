my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(my_list)
while a >0:
    b = int(my_list.pop(0))
    if b > 0:
        print(b)
        a = len(my_list)
    else:
        if b == 0:
            a = len(my_list)
        else:break








