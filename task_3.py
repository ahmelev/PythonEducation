#
# for i in range(1, 101):
#     if (1 < i % 10 < 5) or (i % 10 == 0):
#         print(f"{i} процента")
#     elif 5 <= i % 10 <= 9:
#         print(f"{i} процентов")
#     else:
#         print(f"{i} процент")


for i in range(1, 101):
    if (5 <= i % 10 <= 9) or (10 <= i <= 14):
        print(f"{i} процента")
    elif (1 < i % 10 < 5) or (i % 10 == 0):
        print(f"{i} процентов")
    else:
        print(f"{i} процент")


# percent = input("Введите целое число: ")
# if isinstance(percent, int):
#     if percent > 0:
#         if (1 < percent % 10 < 5) or (percent % 10 == 0):
#             print(f"{percent} процента")
#         elif 5 <= percent % 10 <= 9:
#             print(f"{percent} процентов")
#         else:
#             print(f"{percent} процент")
#     else:
#         print("Вы ввели отрицательное число!")
# else:
#     print("Вы ввели не число число или не целое число!")

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
