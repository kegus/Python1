# 1. Функция деления 2х аргументов
def dev_2(a, b):
    if b == 0:
        raise ZeroDivisionError('На ноль не делим')
    return a / b


while True:
    try:
        num1, num2 = map(int, input('Введите 2 числа: ').split())
        print(dev_2(num1, num2))
    except ZeroDivisionError as e:
        print('На ноль можно делить только после 18 лет.', str(e))
    except Exception as e:
        print("Error! " + str(e))
        break
