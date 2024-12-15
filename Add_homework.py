number = int(input('Введите число от 3 до 20 : '))
password = []
password_1 = []
for i in range(1,number):    # Перебор первого числа в паре
    for j in range(1,number):    # Перебор второго числа в паре
        if number % (i+j) == 0 and i != j:
            password_1 = [i] + [j] # Объединение первого и второго числа в один список
            password_1.sort()       # сортировка чисел в списке по возростанию
            password_1 = map(str,password_1)
            password_1 = ''.join(password_1)   # С помощью метода (map\join) соединяем числа
            password.append(password_1)
set_password = set(password)    #переводим во множество( убираем одинаковые значения)
list_password = list(set_password) # обратно в список

# Сортировка внутри списка
password_2=[]
result = []
result_1 = []

for i in range(1,number-1): # i перебираем от 1 до number-1 (в паре нет 0 и самого значения)
    result_1.sort()
    result = result + result_1
    result_1 = []
    for j in list_password:   # присваиваем переменной j поочередно значения списка
        if int(j[0][0]) == i:  #  первая цифра значения переменной j == i
            j = int(j)
            password_2.append(j)
            result_1 = result_1 + password_2
            password_2 = []
result = map(str,result)
result = ''.join(result)
print(result)