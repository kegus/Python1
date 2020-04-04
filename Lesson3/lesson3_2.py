# 2. Функция информация о пользователе одной строкой
def print_info(**kwargs):
    result = ''
    for key, val in kwargs.items():
        result += key + ' = ' + str(val) + ' '
    return result


# input_dict = {'имя': 'Пётр', 'фамилия': 'Пётров', 'год рождения': 2000, 'город проживания': 'Almaty',
#               'email': 'net_u@menya.email.ru', 'телефон': '88002353535'}
print(print_info(name='Пётр', surname='Пётров'))
print(print_info(name='Пётр', surname='Пётров', birth_year=1999, city='Almaty'))
print(print_info(name='Пётр', surname='Пётров', birth_year=1999, city='Almaty', email='net_u@menya.email.ru',
                 phone='88002353535'))
