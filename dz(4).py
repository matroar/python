number = int(input('Введите целое положительное число: '))
highest_number = number % 10
number = number // 10
while number > 0:
    if number % 10 > highest_number:
        highest_number = number % 10
    number = number // 10
print(highest_number)

