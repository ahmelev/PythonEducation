# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, dividend, divider):
        self.divider = dividend
        self.denominator = divider

    def divide_by_null(dividend, divider):
        try:
            return int(dividend) / int(divider)
        except:
            return "Ошибка! Вы пытаетесь разделить на ноль!"


print(DivisionByNull.divide_by_null(input("Введите делимое: "), input("Введите делитель: ")))
