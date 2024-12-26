def calculate_structure_sum(data_structure):
    result_1 = 0
    #print(*data_structure)
    for j in data_structure:
        my_tuple = ()
        if len(j) > 1:
            for i in data_structure:
                # print(i)
                if isinstance(i, list) == True:
                    my_tuple = my_tuple + tuple(i)
                    # print(my_tuple)
                if isinstance(i, dict) == True:
                    for key in i:
                        my_tuple = my_tuple + tuple(key) + tuple(str(i[key]))
                        # print(my_tuple)
                        # print(type(i[key]))
                if isinstance(i, tuple) == True:
                    my_tuple = my_tuple + i
                    # print(my_tuple)
                if isinstance(i, str) == True:
                    my_tuple = my_tuple + tuple(i)
                    # print(my_tuple)
                if isinstance(i, set) == True:
                    my_tuple = my_tuple + tuple(i)
                if isinstance(i, int) == True:
                    result_1 = result_1 + i

        data_structure = my_tuple
        #print(data_structure)

    data_tuple = ()

    for y in data_structure:
        if isinstance(y, str):
            data_tuple = data_tuple + (y,)
            list_1 = [*data_tuple]
        if isinstance(y, int):
            result_1 = result_1 + y

    #print(result_1)
    for z in list_1:
        a = z.isnumeric()
        # print(a , z)
        if a == True:
            result_1 = result_1 + int(z)
        else:
            result_1 = result_1 + len(z)
    #print(result_1)

    return result_1

data_structure = ([

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])
])

result = calculate_structure_sum(data_structure)
print(result)

