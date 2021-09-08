# (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в
# ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
# использовать в ответе функции?

from requests import get, utils
from decimal import Decimal
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings).split("</Value></Valute>")

currency_date = datetime.strptime(content[0][content[0].find("Date")+6:content[0].find("Date")+16], "%d.%m.%Y").date().strftime(f"%d %B %Y")


def currency_rates(currency):
    for i in content:
        if i.find(currency.upper()) > 0:
            return Decimal(i[i.find("<Value>")+7:].replace(",", "."))


# print(currency_rates(input("Введите один код валюты: ")))
print(f" Курс запрашиваемой валюты = {currency_rates('eur')} на {currency_date}")
print(f" Курс запрашиваемой валюты = {currency_rates('usd')} на {currency_date}")
print(f" Курс запрашиваемой валюты = {currency_rates('sdgsd')} на {currency_date}")
