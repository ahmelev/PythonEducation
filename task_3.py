# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#   ...
#  |--templates
#   |   |--mainapp
#   |   |  |--base.html
#   |   |  |--index.html
#   |   |--authapp
#   |      |--base.html
#   |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные
# ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil

project_name = "my_project"

try:
    for root, dirs, files in os.walk(project_name):
        if "templates" in dirs and root != project_name:
            for i in os.listdir(os.path.join(root, "templates")):
                shutil.copytree(os.path.join(root, "templates", i), os.path.join(project_name, "templates", i))
except FileExistsError:
    print("Дирректория 'templates' уже создана!")
