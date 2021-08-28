for i in range(1, 101):
    if (1 < i < 5) \
            or (21 < i < 25) \
            or (31 < i < 35) \
            or (41 < i < 45) \
            or (51 < i < 55) \
            or (61 < i < 65) \
            or (71 < i < 75) \
            or (81 < i < 85) \
            or (91 < i < 95):
        print(f"{i} процента")
    elif 5 <= i < 21 \
            or (25 <= i < 31) \
            or (35 <= i < 41) \
            or (45 <= i < 51) \
            or (55 <= i < 61) \
            or (65 <= i < 71) \
            or (75 <= i < 81) \
            or (85 <= i < 91) \
            or 95 <= i:
        print(f"{i} процентов")
    else:
        print(f"{i} процент")

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

percent = int(input("Введите целое число от 1 до 100"))
if 0 < percent < 101:
    if (1 < percent < 5) \
            or (21 < percent < 25) \
            or (31 < percent < 35) \
            or (41 < percent < 45) \
            or (51 < percent < 55) \
            or (61 < percent < 65) \
            or (71 < percent < 75) \
            or (81 < percent < 85) \
            or (91 < percent < 95):
        print(f"{percent} процента")
    elif 5 <= percent < 21 \
            or (25 <= percent < 31) \
            or (35 <= percent < 41) \
            or (45 <= percent < 51) \
            or (55 <= percent < 61) \
            or (65 <= percent < 71) \
            or (75 <= percent < 81) \
            or (85 <= percent < 91) \
            or 95 <= percent:
        print(f"{percent} процентов")
    else:
        print(f"{percent} процент")
else:
    print("Вы ввели некорректное число!")
