# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

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
