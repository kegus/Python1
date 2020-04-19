# 2. Одежда, пальто и костюм

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def calc_fabric_consumption(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def calc_fabric_consumption(self):
        return self.H * 2 + 0.3


while True:
    clothes_type = int(input('Выберите тип, пальто (1) или костюм (2): '))
    if clothes_type == 1:
        coat_size = float(input('Введите размер пальто: '))
        clothes = Coat(coat_size)
    elif clothes_type == 2:
        suit_height = float(input('Введите размер пальто: '))
        clothes = Suit(suit_height)
    else:
        print('Неверный тип')
        break
    print(f'Нужно {clothes.calc_fabric_consumption:.2f} ткани')
