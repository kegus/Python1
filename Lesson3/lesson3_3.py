# 3. Функция 3х аргументов возвращает максимальную сумму 2x
def my_func(*args):
    if len(args) != 3:
        raise IndexError('Не верное число аргументов')
    for val in args:
        if type(val) != int:
            raise TypeError('Не верный тип аргументов')
    max_sum = 0
    for val in args:
        check_sum = sum(args) - val
        if check_sum > max_sum:
            max_sum = check_sum
    return max_sum


try:
    print(my_func(4, 2, 3))
except Exception as e:
    print(str(e))
