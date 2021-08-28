# Задание А
list_kub = []
all_sum = 0

for i in range(1, 1001, 2):
    list_kub.append(i**3)

for n in list_kub:
    first_sum = n
    n_sum = 0
    while n > 0:
        one_meaning = n % 10
        n_sum += one_meaning
        n = n // 10
    if n_sum % 7 == 0:
        print(f"Сумма числа {first_sum} = {n_sum} и она кратна 7")
        all_sum += first_sum

print(f"Сумма всех чисел кратных 7 = {all_sum}")

# Задание Б
all_sum = 0
new_list_kub = []

for i in list_kub:
    new_list_kub.append(i+17)

for n in new_list_kub:
    first_sum = n
    n_sum = 0
    while n > 0:
        one_meaning = n % 10
        n_sum += one_meaning
        n = n // 10
    if n_sum % 7 == 0:
        print(f"Сумма числа {first_sum} = {n_sum} и она кратна 7")
        all_sum += first_sum

print(f"Сумма всех чисел кратных 7 = {all_sum}")

# Скорее всего неправильно понял сути задачи со звездочкой, но вот его решение
all_sum = 0
list_kub = []
for i in range(1, 1001, 2):
    list_kub.append(i**3)

for n in list_kub:
    first_sum = n
    new_first_sum = n+17
    new_n = n+17
    n_sum = 0
    while new_n > 0:
        one_meaning = new_n % 10
        n_sum += one_meaning
        new_n = new_n // 10
    if n_sum % 7 == 0:
        print(f"Сумма числа {new_first_sum} = {n_sum} и она кратна 7")
        all_sum += new_first_sum

print(f"Сумма всех чисел кратных 7 = {all_sum}")



# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X): Вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в
# сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции! К 
# каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится 
# нацело на 7. * Решить задачу под пунктом b, не создавая новый список.
