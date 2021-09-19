# * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг
# данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
# преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа.
# Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в результате
# парсинга.

from itertools import zip_longest

users = []
hobby = []


with open("users.csv", "r", encoding="utf-8") as u:
    for line in u.readlines():
        users.append(line.replace("\n", "").replace(",", " "))


with open("hobby.csv", "r", encoding="utf-8") as h:
    for line in h.readlines():
        hobby.append(line.replace("\n", ""))

if len(users) >= len(hobby):
    users_hobby = dict(zip_longest(users, hobby[:len(users)]))
    with open("users-hobby.csv", "w", encoding="utf-8") as uh:
        uh.writelines(f"{users_hobby} \n")
else:
    exit(1)

