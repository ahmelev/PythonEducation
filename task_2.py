# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two") "два"


num_translate_adv = \
    {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }


def num_translate(*args):
    if num[0].islower():
        if str(num).lower() in num_translate_adv.keys():
            print(num_translate_adv.get(num.lower()))
    else:
        if str(num).lower() in num_translate_adv.keys():
            print(num_translate_adv.get(num.lower()).capitalize())


num = input("Введите значение: ")

num_translate(num)
