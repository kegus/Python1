# Рентабельность фирмы
profit = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
#print(f'Фирма работает с {"прибылью" if profit > expenses else "убытком"}')
if profit > expenses:
    print('Фирма работает с "прибылью"')
    print(f'Рентабельность: {(profit - expenses) / profit}')
    cnt_emploes = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на сотрудника равна {(profit - expenses) / cnt_emploes}')
else:
    print('Фирма работает с "убытком"')
