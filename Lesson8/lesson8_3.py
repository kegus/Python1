# 2. Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел

class MyCheckNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyListNumbers(list):
    def my_append(self, number):
        try:
            number = float(number)
            self.append(number)
        except Exception as e:
            raise MyCheckNumbers('Можно добавлять только числа')


my_list = MyListNumbers()
while True:
    try:
        my_num = input('Введите число: ')
        if my_num.lower() == 'stop':
            break
        my_list.my_append(my_num)
    except MyCheckNumbers as e:
        print(e)

print(my_list)
