# SportsMan
print('Введите a и b')
a, b = (int(input()) for _ in range(2))

c = 10.0 # Процент увеличения

cnt_day = 1
while a < b:
    print(f'День {cnt_day} - {a} километров')
    a = float(a + a * c / 100)
    cnt_day += 1
print(f'День {cnt_day} - {a} километров')

print(f'Ответ: {cnt_day} день')