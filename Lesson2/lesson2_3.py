# 3. На вход номер месяца - на выход время года (2 способа)
month_list = (('Январь', 'Зима'), ('Февраль', 'Зима'), ('Март', 'Весна'),
              ('Апрель', 'Весна'), ('Май', 'Весна'), ('Июнь', 'Лето'),
              ('Июль', 'Лето'), ('Август', 'Лето'), ('Сентябрь', 'Осень'),
              ('Октябрь', 'Осень'), ('Ноябрь', 'Осень'), ('Декабрь', 'Зима'))
month_dict = {1: ('Январь', 'Зима'), 2: ('Февраль', 'Зима'), 3: ('Март', 'Весна'),
              4: ('Апрель', 'Весна'), 5: ('Май', 'Весна'), 6: ('Июнь', 'Лето'),
              7:('Июль', 'Лето'), 8:('Август', 'Лето'), 9: ('Сентябрь', 'Осень'),
              10: ('Октябрь', 'Осень'), 11: ('Ноябрь', 'Осень'), 12: ('Декабрь', 'Зима')}
month_num = int(input('Введите номер месяца: '))

print('1й способ')
print(month_list[month_num-1])
print('2й способ')
print(month_dict.get(month_num))