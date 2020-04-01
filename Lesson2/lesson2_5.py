# 5. Структура Рейтинг
rate_list = [7, 5, 3, 3, 2]
rate_list1 = rate_list.copy()
rate_list2 = rate_list.copy()
while True:
    new_rate = int(input('Введите новый рейтинг: '))
    if new_rate == 0:
        break
    #1-й способ
    print('1-й способ')
    print(rate_list1)
    for n, rate in enumerate(rate_list1):
        if new_rate > rate:
            rate_list1.insert(n, new_rate)
            break
    print(rate_list1)

    #2-й способ
    print('2-й способ')
    rate_list2.append(new_rate)
    print(rate_list2)
    rate_list2.sort(reverse=True)
    print(rate_list2)