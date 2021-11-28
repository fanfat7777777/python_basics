first_list = []

#Создать список, состоящий из кубов нечётных чисел от 1 до 1000
for i in range(1, 1000):
    if i % 2 != 0:
        number = i**3
        first_list.append(number)

print(first_list)


# Задача a - Проверяем деление на 7 и считаем сумму чисел
sum_number = 0
for i in range(0, len(first_list)):

    number = first_list[i]
    amount = 0
    
    while (number != 0):
        amount = amount + number % 10
        number = number // 10

    if amount % 7 == 0:
        sum_number += first_list[i]

print('а)', sum_number)

# Задача b - Прибавляем 17, проверяем деление на 7 и считаем сумму
sum_number = 0
for i in range(0, len(first_list)):

    number = first_list[i] + 17
    amount = 0
    while (number != 0):
        amount = amount + number % 10
        number = number // 10

    if amount % 7 == 0:
        sum_number += first_list[i]

print('b)', sum_number)