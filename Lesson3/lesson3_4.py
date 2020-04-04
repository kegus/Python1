# 4. Возведение в отрицательную степень
def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    val = x
    pow = abs(y) - 1
    for _ in range(pow):
        val *= x
    return 1 / val


while True:
    try:
        x = float(input('Введите действительное положительное число: '))
        if x <= 0:
            raise ValueError('Число должно быть положительным')
        y = int(input('Введите целое отрицательное число: '))
        if y >= 0:
            raise ValueError('Число должно быть отрицательным')
        print(my_func1(x, y))
        print(my_func2(x, y))
    except Exception as e:
        print(str(e))
        break
