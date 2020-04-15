# 3. Worker -> Position

class Worker:
    _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname, self.position

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


name, surname, position = input("Введите имя, фамилию и должность: ").split()
wage, bonus = map(int, input("Введите оклад и премию: ").split())

position = Position(name, surname, position, wage, bonus)
print(f"ФИ: {position.get_full_name()}")
print(f"Доход: {position.get_total_income()}")
