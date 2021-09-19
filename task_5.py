# ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим
# исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы
# находятся в разных папках.

from itertools import zip_longest
from sys import argv
users = []
hobby = []

f_1, f_2, out_f = argv[1:]

with open(f_1, "r", encoding="utf-8") as u:
    for line in u.readlines():
        users.append(line.replace("\n", "").replace(",", " "))


with open(f_2, "r", encoding="utf-8") as h:
    for line in h.readlines():
        hobby.append(line.replace("\n", ""))

if len(users) >= len(hobby):
    users_hobby = dict(zip_longest(users, hobby[:len(users)]))
    with open(out_f, "w", encoding="utf-8") as uh:
        uh.writelines(f"{users_hobby} \n")
else:
    exit(1)
