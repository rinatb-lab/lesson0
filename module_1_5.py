immutable_var=(1,2,3,'Кортеж',True)
print(immutable_var, ' -кортеж с постоянными элементами ')
#immutable_var[4]=False - При активации выйдет ошибка:
# TypeError: 'tuple' object does not support item assignment (постоянные
# значения элементов кортежа изменить нельзя)
mutable_list=(1,2,3,['Кортеж',True])
print(mutable_list,' -кортеж с постоянными и переменными элементами')
mutable_list[3][1]=False
print(mutable_list, ' -кортеж с постоянными и изменёнными переменными элементами')