#
#5:
# Напишите программу которая принимает число любой длины и вытаскивает из него самое большое и самое маленькое число.
####

numbers = int(input('Vvedite chislo'))
list_numbers = list(str(numbers))
for element in list_numbers:
    max_number = max(list_numbers)
    min_number = min(list_numbers)

print('Максимальное число: ', max_number)
print('Минимальное число: ', min_number)
