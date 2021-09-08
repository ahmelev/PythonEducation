# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
# в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
# лишнего не происходит.

import utils

print(f" Курс запрашиваемой валюты = {utils.currency_rates('BRL')} на {utils.currency_date}")
print(f" Курс запрашиваемой валюты = {utils.currency_rates('inr')} на {utils.currency_date}")
print(f" Курс запрашиваемой валюты = {utils.currency_rates('sdfsdf')} на {utils.currency_date}")
