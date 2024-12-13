def get_matrix(n=2,m=2,value=10):
    matrix = []
    for i in range(0, n):
        matrix_1 = []
        for j in range(m):
            matrix_1.append(value)
        matrix.append(matrix_1)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print('result1 : ',result1)
print('result1 : ',result2)
print('result1 : ',result3)








