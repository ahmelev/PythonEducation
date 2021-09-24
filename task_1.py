# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.
#
# https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
# turtle или PyQT5 - библиотека для рисования
from time import sleep


class TrafficLight:
    __color = ["красный", "жёлтый", "зелёный"]

    def running(self):
        pass

    def running(self):
        for i in range(len(self.__color)):
            print(f'Сигнал сфетофора - {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)


trafficlight = TrafficLight()
trafficlight.running()
