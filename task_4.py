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


class Scanner(OfficeEquipment):

    def __init__(self, name, price, quantity, speed_scan):
        super().__init__(name, price, quantity)
        self.speed_scan = speed_scan


class Copier(OfficeEquipment):

    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size
