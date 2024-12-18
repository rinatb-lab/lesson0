def print_params(a = 1, b = 'Строка', c = True):
    print(a,b,c)

print_params()
# Распаковка:
print_params(b = 25)
print_params(c = [1,2,3])
print('')
# Распаковка параметров:
values_list = [1 , 'Строка' , [1,2,3]]
values_dict = {'a' : [1,2,3] , 'b' : 'Строка', 'c' :  1}
print_params(*values_list)
print_params(**values_dict)
print('')
# Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


