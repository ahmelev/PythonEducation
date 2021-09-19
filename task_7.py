# 7. Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
""" тут находится второй скрипт для считывания информации """
from sys import argv


with open("ballance.txt", "r", encoding="utf-8") as m:
    if len(argv) == 1:
        print(m.read())
    elif len(argv) == 2:
        print(m.readlines()[int(argv[1])-1:])
    elif len(argv) == 3:
        print(m.readlines()[int(argv[1])-1:int(argv[2])])
