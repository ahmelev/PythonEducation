# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
# комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

# https://xn--24-6kcaa2awqnc8dd.xn--p1ai/umnozhenie-kompleksnyh-chisel.html

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z1 = {self.a + other.a} + z2 = {self.b + other.b} = {(self.a + other.a) + (self.b + other.b)}'

    def __mul__(self, other):
        return f'z1 = {(self.a * other.a) - (self.b * other.b)} + z2 = {(self.b * other.a)+(self.a * other.b)} = ' \
               f'{((self.a * other.a) - (self.b * other.b)) + ((self.b * other.a)+(self.a * other.b))}'


z_1 = ComplexNumber(1, 2)
z_2 = ComplexNumber(3, 4)

print(z_1 + z_2)
print(z_1 * z_2)

