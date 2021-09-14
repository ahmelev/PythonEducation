# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

from collections import Counter, defaultdict

"""выводятся все, самый первый в списке наш товарищ, так я и не понял как достать один элемент из 
полученного типа данных <class 'collections.Counter'>"""

my_real_list = []

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        my_list = line[:line.find(" ")]
        my_real_list.append(my_list)
spammer = max(Counter(my_real_list).items(), key=lambda x: x[1])
print(spammer)
