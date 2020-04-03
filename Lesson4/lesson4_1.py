# 1. Расчёт зарабтной платы
from sys import argv


def calc_salary(args):
    print(args)
    hours, bet, bonus = args
    return (hours * bet) + bonus


print(len(argv))
print(argv[1:])
if len(argv) != 4:
    print('Неверное число параметров')
else:
    print('ЗП сотрудника: ', calc_salary(list(map(int, argv[1:]))))
