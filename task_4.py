# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
#
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
import collections

dir_project = "some_data"
files_project = collections.defaultdict(int)

for root, dirs, files in os.walk(dir_project):
    for f in files:
        size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))
        files_project[size] += 1

print(files_project)
