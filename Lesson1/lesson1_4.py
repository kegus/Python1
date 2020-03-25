# 4. Найти макс. число
complex_num = input('Введите число: ')
a_max = 0
i = 0
while i < len(complex_num):
    a_check = int(complex_num[i])
    i += 1;
    if a_check > a_max:
        a_max = a_check
print(a_max)