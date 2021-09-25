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
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышает скоростной режим'
        else:
            return f'{super().show_speed()}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} превышает скоростной режим'
        else:
            return f'{super().show_speed()}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car_1 = TownCar(50, "blue", "Taxi", False)
town_car_2 = TownCar(70, "black", "Autobuss", False)
sport_car = SportCar(100, "red", "Sport", False)
work_car_1 = WorkCar(30, "green", "Avtomoika", False)
work_car_2 = WorkCar(50, "yellow", "Snowcliner", False)
police_car = PoliceCar(90, "police_color", "Police car", True)

print(f'{town_car_1.name}, {town_car_1.color}, полицейская машина? - {"Нет" if town_car_1.is_police == False else "Да"}')
print(town_car_1.go())
print(town_car_1.show_speed())
print(town_car_1.turn())
print(town_car_1.stop())
print("*" * 30)

print(f'{town_car_2.name}, {town_car_2.color}, полицейская машина? - {"Нет" if town_car_2.is_police == False else "Да"}')
print(town_car_2.go())
print(town_car_2.show_speed())
print(town_car_2.turn())
print(town_car_2.stop())
print("*" * 30)

print(f'{sport_car.name}, {sport_car.color}, полицейская машина? - {"Нет" if sport_car.is_police == False else "Да"}')
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.turn())
print(sport_car.stop())
print("*" * 30)

print(f'{work_car_1.name}, {work_car_1.color}, полицейская машина? - {"Нет" if work_car_1.is_police == False else "Да"}')
print(work_car_1.go())
print(work_car_1.show_speed())
print(work_car_1.turn())
print(work_car_1.stop())
print("*" * 30)

print(f'{work_car_2.name}, {work_car_2.color}, полицейская машина? - {"Нет" if work_car_2.is_police == False else "Да"}')
print(work_car_2.go())
print(work_car_2.show_speed())
print(work_car_2.turn())
print(work_car_2.stop())
print("*" * 30)

print(f'{police_car.name}, {police_car.color}, полицейская машина? - {"Нет" if police_car.is_police == False else "Да"}')
print(police_car.go())
print(police_car.show_speed())
print(police_car.turn())
print(police_car.stop())
print("*" * 30)