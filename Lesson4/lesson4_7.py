# 7. Реализовать генератор с помощью функции с ключевым словом yield


def fact(num):
    num += 1
    res = 1
    for el in range(1, num):
        res *= el
        yield res


n = int(input('Введите число: '))
prev_el = 1
for el in fact(n):
    print(f'{el // prev_el}! = {el}')
    prev_el = el
