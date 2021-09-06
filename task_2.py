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


def num_translate(num):
    if num[0].islower():
        if num in num_translate_adv:
            print(num_translate_adv.get(num))
    else:
        if num.lower() in num_translate_adv:
            print(num_translate_adv.get(num.lower()).capitalize())


num_translate(input("Введите значение: "))
