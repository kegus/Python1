# 4. Car TownCar SportCar WorkCar PoliceCar

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, "поехала")

    def stop(self):
        print(self.name, "остановилась")

    def turn(self, direction):
        print(self.name, "повернула", direction)

    def show_speed(self):
        print(self.name, "скороть", self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(self.name, "превысила скорость")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(self.name, "превысила скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car1 = TownCar(50, "red", "Жигули")
town_car2 = TownCar(70, "yellow", "Запорожец")
sport_car = SportCar(100, "green", "Инвалидка")
work_car1 = WorkCar(35, "brown", "Москвич")
work_car2 = WorkCar(45, "black", "Волга")
police_car = PoliceCar(80, "blue", "Жигули(П)")

town_car1.go()
town_car2.stop()
sport_car.turn("налево")
work_car1.turn("направо")
police_car.show_speed()
town_car1.show_speed()
town_car2.show_speed()
work_car1.show_speed()
work_car2.show_speed()
