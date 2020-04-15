# 5. Stationery

class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(self.title, "Запуск отрисовки. Pen")


class Pencil(Stationery):
    def draw(self):
        print(self.title, "Запуск отрисовки. Pencil")


class Handle(Stationery):
    def draw(self):
        print(self.title, "Запуск отрисовки. Handle")


stationery = Stationery()
stationery.draw()

pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()
