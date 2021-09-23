# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
# конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os
path = r'/Users/aleksandrhmelev/PycharmProjects/PythonEducation'
project_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']


def crate_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


fullPath = os.path.join(path, project_name)
crate_folder(fullPath)

for i in folders:
    folder = os.path.join(fullPath, i)
    crate_folder(folder)
