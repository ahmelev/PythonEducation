# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract_method(cls, day_month_year):
        date = []

        for i in day_month_year.split("-"):
            date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validator(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if str(year).isdigit and 2221 >= year >= 0:
                    return f'Введены корректные значения'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Переданная дата - {Data.extract_method(self.day_month_year)}'


print(Data('02-05-1985'))

print(Data.extract_method('05-10-2021'))

print(Data.validator(1, 11, '2000'))
