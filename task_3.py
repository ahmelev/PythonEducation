# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят,
# in place). Эта задача намного серьёзнее, чем может сначала показаться.

# Вроде как это решение

text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, n in enumerate(text_list):
    if n.isdigit():
        text_list[i] = f'"{int(n):02}"'
        print(i)
    else:
        if n.find('+') != -1 or n.find('-') != -1:
            text_list[i] = f'"{n[:1]}{int(n[1:]):02}"'
print(text_list)

text = " ".join(text_list)
print(text)
