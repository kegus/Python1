# 6. Два небольших скрипта
from itertools import count, cycle


def max_num():
    return 20


def max_copy():
    return 5


start_num = int(input('Введите начальное число: '))


# a) итератор, генерирующий целые числа, начиная с указанного
def make_list(start, max):
    res = []
    for el in count(start):
        if el > max:
            break
        else:
            res.append(el)
    return res


res_list = make_list(start_num, max_num())
print(res_list)


# b) итератор, повторяющий элементы некоторого списка
def make_list(input_list, n_copy):
    res = []
    cnt = 0
    cnt_copy = 0
    for el in cycle(input_list):
        if cnt_copy >= n_copy:
            break
        else:
            res.append(el)
            cnt += 1
            cnt_copy = cnt // len(input_list)
    return res


res_list = make_list(res_list, max_copy())
print(res_list)
