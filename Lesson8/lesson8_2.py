# 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на нуль

class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyCheckClass:
    def my_division(self, a, b):
        if b == 0:
            raise MyZeroDivisionError('На ноль не делим')
        else:
            return a / b


my_check_class = MyCheckClass()
try:
    print(my_check_class.my_division(9, 3))
except MyZeroDivisionError as e:
    print(e)

try:
    print(my_check_class.my_division(7, 0))
except MyZeroDivisionError as e:
    print(e)
