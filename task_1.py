# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one") "один" >>> num_translate("eight") "восемь" Если перевод сделать невозможно, вернуть None.

# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции
# или снаружи.

translate_dict = \
    {
        "Zero": "Ноль",
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять",
        "Six": "Шесть",
        "Seven": "Семь",
        "Eight": "Восемь",
        "Nine": "Девять",
        "Ten": "Десять"
    }


def num_translate(*args):
    for i in translate_dict:
        if num in str(i):
            print(translate_dict.get(i, 'Значение не найдено'))


num = input("Введите значение: ")

num_translate(num)
