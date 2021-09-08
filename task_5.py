#  (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05


from requests import get, utils
from decimal import Decimal
from datetime import datetime
import locale
from sys import argv

locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings).split("</Value></Valute>")

currency_date = datetime.strptime(content[0][content[0].find("Date") + 6:content[0].find("Date") + 16],
                                  "%d.%m.%Y").date().strftime(f"%d %B %Y")

_, currency = argv


def currency_rates(currency):
    for i in content:
        if i.find(currency.upper()) > 0:
            return Decimal(i[i.find("<Value>") + 7:].replace(",", "."))


print(f" Курс запрашиваемой валюты = {currency_rates(currency)} на {currency_date}")
