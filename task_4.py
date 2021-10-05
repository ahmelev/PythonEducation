# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте
# параметры, уникальные для каждого типа оргтехники.

class Storage:

    def __init__(self):
        self.my_store = []

    def reception(self):
        pass


class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):

    def __init__(self, name, price, quantity, speed_print):
        super().__init__(name, price, quantity)
        self.speed_print = speed_print

    def to_print(self):
        return f'Печатает {self.speed_print} листов в минуту'


class Scanner(OfficeEquipment):

    def __init__(self, name, price, quantity, speed_scan):
        super().__init__(name, price, quantity)
        self.speed_scan = speed_scan

    def to_scan(self):
        return f'Сканирует {self.speed_scan} листов в минуту'


class Copier(OfficeEquipment):

    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def to_copier(self):
        return f'Ксерокс  {self.size}'
