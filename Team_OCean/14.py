# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
#     и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#####################################################################

while True:
    season = int(input('Введите номер месяца (1-12) '))
    if season <= 0 or season > 12:
        print('От 1 до 12')
    if season == 1 or season == 2 or season == 12:
        print('Зима')
        break
    if season > 2 and season <= 5:
        print('Весна ')
        break
    if season > 5 and season <= 8:
        print("Лето ")
        break
    if season > 8 and season <= 11:
        print('Осень')
        break

