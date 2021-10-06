# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storage:

    def __init__(self, name):
        self.name = name
        self.my_store = {}

    def reception(self, equipment):
        self.my_store.setdefault(equipment.group_name(), []).append(equipment)

    def transfer(self, type, store):
        if self.my_store[type]:
            store.my_store.setdefault(type, []).append(self.my_store.setdefault(type).pop(0))


class OfficeEquipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.group = self.__class__.__name__

    def __repr__(self):
        return f'{self.name} {self.price}'

    def group_name(self):
        return f'{self.group}'


class Printer(OfficeEquipment):

    def __init__(self, name, price, speed_print):
        super().__init__(name, price)
        self.speed_print = speed_print

    def __repr__(self):
        return f'{self.name} {self.price} {self.speed_print}'


class Scanner(OfficeEquipment):

    def __init__(self, name, price, speed_scan):
        super().__init__(name, price)
        self.speed_scan = speed_scan

    def __repr__(self):
        return f'{self.name} {self.price} {self.speed_scan}'


class Copier(OfficeEquipment):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __repr__(self):
        return f'{self.name} {self.price} {self.size}'


""" создаем объекты """
printer_hp = Printer("HP", 3940.40, 100)
printer_xerox = Printer("Xerox", 2500.80, 95)
printer_epson = Printer("Epson", 3000.00, 90)
scanner_hp = Scanner("HP", 2600.50, 6)
scanner_xerox = Scanner("Xerox", 2900.00, 5)
scanner_epson = Scanner("Epson", 1900.90, 7)
copier_hp = Copier("HP", 6700.00, "Большой")
copier_xerox = Copier("Xerox", 7300.00, "Маленький")
copier_epson = Copier("Epson", 7100.60, "Большой")
basic_storage = Storage("Основной склад")
subdivision_one = Storage("Подразделение 1")
subdivision_two = Storage("Подразделение 2")
subdivision_three = Storage("Подразделение 3")

""" для удобства помещения их на склад запихиваем в одну переменную """
all_office_equipment = (printer_hp, printer_xerox, printer_epson, scanner_hp, scanner_xerox, scanner_epson, copier_hp,
                        copier_xerox, copier_epson)
""" собственно помещаем на склад """
for i in all_office_equipment:
    basic_storage.reception(i)

""" смотрим что на складе """
print(basic_storage.my_store)
print()

""" перемещаем по типу оборудования первую в списке единицу техники в подразделение компании и выводим результат """
basic_storage.transfer('Scanner', subdivision_one)
print()
print(basic_storage.my_store)
print()
print(subdivision_one.my_store)

basic_storage.transfer('Copier', subdivision_two)
print()
print(basic_storage.my_store)
print()
print(subdivision_two.my_store)

basic_storage.transfer('Printer', subdivision_three)
print()
print(basic_storage.my_store)
print()
print(subdivision_three.my_store)
