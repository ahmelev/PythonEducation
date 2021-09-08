# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP,
# ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
# браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
# того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils


# def currency_rates():
#     pass


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings).split("</Value></Valute>")
# print(content)


def currency_rates(currency):
    for i in content:
        one_content = i
        if one_content.find(currency) > 0:
            print(i.find("<Value>"))
            print(i[i.find("<Value>")+7:])
            print(one_content)


# for i, v in enumerate(content):
#     if currency in content[i][v]:
#         print(content[i].find("<Value>"))
#         print(str(content[i])[content[i].find("<Value>")+7:])
#         print(content[i])


print(currency_rates(input("Введите код валюты: ")))
