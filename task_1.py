duration = int(input("Введите число: "))

day = duration // (60*60*24)
duration %= (60*60*24)
hours = duration // (60*60)
duration %= (60*60)
minutes = duration // 60
duration %= 60

print(f"Из введенного числа получается {day} дн {hours} час {minutes} мин {duration} сек")
