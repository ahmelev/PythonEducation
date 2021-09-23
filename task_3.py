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

def type_logger(func):
    print(func)

    def real_logger(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        for a in args:
            type_value = func(a)
            print(f'{a}: {type(a)}')
        for k, w in kwargs.items():
            type_value = func(w)
            print(f'{w}: {type(w)}')
        return type_value

    return real_logger


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(8, 6, one="8844", two="443")
