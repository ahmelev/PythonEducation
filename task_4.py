# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например:
#
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

""" Задача выполнена только после просмотра решения, не додумался что лямбда это тоже функция и ее надо обработать"""

import functools


def val_checker(lambda_func):
    def real_val_checker(func):

        @functools.wraps(func)
        def checker(num):
            if lambda_func(num):
                print(func(num))
            else:
                raise ValueError(f'Введено некорректное число {num}')

        return checker

    return real_val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
b = calc_cube(-5)
