# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для
# каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for i in range(1, 101):
    if (1 < i % 10 < 5) and (i != 12) and (i != 13) and (i != 14):
        print(f"{i} процента")
    elif (i % 10 == 1) and (i != 11):
        print(f"{i} процент")
    else:
        print(f"{i} процентов")

# percent = int(input("Введите целое число: "))
# if percent > 0:
#     if (1 < percent % 10 < 5) and (percent != 12) and (percent != 13) and (percent != 14):
#         print(f"{percent} процента")
#     elif (percent % 10 == 1) and (percent != 11):
#         print(f"{percent} процент")
#     else:
#         print(f"{percent} процентов")
# else:
#     print("Вы ввели отрицательное число!")
