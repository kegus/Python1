# 1. Реализовать класс «Дата»

class MyData:
    dd, mm, yyyy = (None, None, None)

    @classmethod
    def decode(cls, data):
        cls.validate(data)
        data_list = dict()
        data_list['dd'] = cls.dd
        data_list['mm'] = cls.mm
        data_list['yyyy'] = cls.yyyy
        return data_list

    @staticmethod
    def validate(data):
        res = False
        try:
            MyData.dd, MyData.mm, MyData.yyyy = map(int, data.split('.'))
            if MyData.dd > 0 and MyData.mm > 0 and MyData.yyyy > 0 and (
                    (MyData.mm == 1 and MyData.dd < 32) or (MyData.mm == 10 and MyData.dd < 32) or
                    (MyData.mm == 11 and MyData.dd < 31) or (MyData.mm == 12 and MyData.dd < 32) or
                    (MyData.mm == 2 and MyData.dd < 29) or (MyData.mm == 3 and MyData.dd < 32) or
                    (MyData.mm == 4 and MyData.dd < 31) or (MyData.mm == 5 and MyData.dd < 32) or
                    (MyData.mm == 6 and MyData.dd < 31) or (MyData.mm == 7 and MyData.dd < 32) or
                    (MyData.mm == 8 and MyData.dd < 32) or (MyData.mm == 9 and MyData.dd < 31)):
                res = True
            else:
                MyData.dd, MyData.mm, MyData.yyyy = (None, None, None)
        except Exception as e:
            MyData.dd, MyData.mm, MyData.yyyy = (None, None, None)
            print('Неверная дата')
        return res


while True:
    my_data = input(f'Введите дату: ')
    print(MyData.decode(my_data))
    should_continue = MyData.validate(my_data)
    print(f'Дата правильная: {should_continue}')
    if not should_continue:
        break
