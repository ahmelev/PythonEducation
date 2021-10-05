# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

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
