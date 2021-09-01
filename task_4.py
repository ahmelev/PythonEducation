# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет,
# Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли
# при этом не создавать новый список?

start_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                         'аэлита']
for i, v in enumerate(start_list):
    idx = v.rfind(' ')
    name = v[idx+1:]
    start_list[i] = f'Привет, {name.capitalize()}!'
print(idx)
print(name)
print(start_list)
