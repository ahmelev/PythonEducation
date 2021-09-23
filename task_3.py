# Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>

# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):
    print(func)

    @wraps(func)
    def real_logger(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        for a in (*args, *kwargs.values()):
            type_value = func(a)
            print(f'{func.__name__}({a}: {type(a)})')
        return type_value

    return real_logger


@type_logger
def calc_cube(x):
    return x


calc_cube(8, 6, one="8844", two="443")
