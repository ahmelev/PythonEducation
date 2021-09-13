# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [i for i in src]
for i in range(1, len(result)):
    if result[i] > result[i - 1]:
        print(result[i])
