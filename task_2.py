# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

my_real_list = []

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        my_list = line[:line.find(" ")], line[line.find('"')+1: line.find(" /")], line[line.find(' /')+1: line.find(" HTTP")]
        my_real_list.append(my_list)

print(my_real_list)
