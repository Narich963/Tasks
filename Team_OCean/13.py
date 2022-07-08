# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа.
#     Требуется положительные поместить в один список, а отрицательные - в другой.
###################################################################

list = [-1, -2413213, 87233, -21331, 5423, -233, 2323, 2323 ,545215, 963, -963]

negative = [i for i in list if i < 0]
positive = [i for i in list if i > 0]
print(negative)
print(positive)

list = []
code = input("Введите числа через пробел ")
code = code.split(' ')
step = int(input('Введите сдвиг '))
for i in range(len(code)):
    if i + step > code:

    else:
        code[i], code[i + step] = code[i + step], code[i]
