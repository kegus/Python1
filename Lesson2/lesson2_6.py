# 6. Структура данных «Товары» и аналитика
goods = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

name_set = set()
cost_set = set()
count_set = set()
unit_set = set()
result = dict()

while True:
    name, cost, count, unit = (None, None, None, None)
    name_set.clear()
    cost_set.clear()
    count_set.clear()
    unit_set.clear()
    result.clear()
    print('Введите через пробел название, цена, количество, eд.измер. \n')
    try:
        name, cost, count, unit = input().split()
        cost = int(cost)
        count = int(count)
    except ValueError:
        name = None
    if not name:
        break
    goods.append((len(goods) + 1, {'название': name, 'цена': cost, 'количество': count, 'eд': unit}))

    for item in goods:
        good = item[1]
        name_set.add(good.get('название'))
        cost_set.add(good.get('цена'))
        count_set.add(good.get('количество'))
        unit_set.add(good.get('eд'))

    result['название'] = name_set
    result['цена'] = cost_set
    result['количество'] = count_set
    result['eд'] = unit_set
    print(result)
