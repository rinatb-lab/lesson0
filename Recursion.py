def get_multiplied_digits(number = 40203):
    str_number = (str(number))
    first = int(str_number[0])
    if first == 0:
        first = 1
    if len(str_number) > 1 :
        first = first * get_multiplied_digits(int(str_number[1:]))
    return first

result = get_multiplied_digits(4020010030)
print(result)
result2 = get_multiplied_digits(4020103)
print(result2)
