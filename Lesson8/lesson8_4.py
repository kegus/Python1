# 4. Склад оргтехники
# 5. Приём оргтехники на склад и передачу в определенное подразделение компании
# 6. Механизм валидации данных

class MyTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.item_list = dict()

    def append(self, item, cnt=1):
        if type(cnt) != int:
            raise MyTypeError

        cnt_item = self.item_list.get(item)
        if cnt_item == None:
            cnt_item = cnt
        else:
            cnt_item += cnt
        self.item_list[item] = cnt_item
        print(item.name, 'добавлен на склад. Всего: ', cnt_item)

    def move(self, other, item, cnt=1):
        if type(cnt) != int:
            raise MyTypeError('Нужно передавать целое число')

        cnt_item = self.item_list.get(item)
        if cnt_item == None or cnt_item - cnt < 0:
            print('Недостаточно товара', item.name)
        else:
            self.item_list[item] = cnt_item - cnt
            print(item.name, 'осталось: ', self.item_list[item])
            other.append(item, cnt)


class Equipment:
    def __init__(self, name, voltage):
        self.name = name
        self.voltage = voltage


class Printer(Equipment):
    def __init__(self, voltage, toner_type):
        super().__init__('Printer', voltage)
        self.toner_type = toner_type


class Scanner(Equipment):
    def __init__(self, voltage, max_width):
        super().__init__('Scanner', voltage)
        self.max_width = max_width


class Copier(Equipment):
    def __init__(self, voltage, cnt_copy_per_min):
        super().__init__('Copier', voltage)
        self.cnt_copy_per_min = cnt_copy_per_min


warehouse1 = Warehouse()
warehouse2 = Warehouse()

printer = Printer(220, 'color')
warehouse1.append(printer, 4)

scanner = Scanner(220, 120)
warehouse1.append(scanner)

copier = Copier(110, 5)
warehouse1.append(copier)

warehouse1.move(warehouse2, printer, 3)
warehouse1.move(warehouse2, scanner, 2)
try:
    warehouse2.move(warehouse1, printer, '3')
except MyTypeError as e:
    print(e)
