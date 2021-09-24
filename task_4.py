# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте экземпляры
# классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите
# результат.

import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} прекратил движение'

    def turn(self):
        direction = ["право", "лево"]
        return f'{self.name} повернул на {random.choice(direction)}'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, is_police)

    def show_speed(self):
        pass


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, is_police)

    def show_speed(self):
        pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, is_police)


town_car_1 = TownCar(50, "blue", "Taxi", False)
town_car_2 = TownCar(70, "black", "Autobuss", False)
sport_car = SportCar(100, "red", "Sport", False)
work_car_1 = WorkCar(30, "green", "Avtomoika", False)
work_car_2 = WorkCar(50, "yellow", "Snowcliner", False)
police_car = PoliceCar(90, "police_color", "Police car", True)