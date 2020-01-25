time = int (input ('Введите время в секундах: '))
minute = (time % 3600)//60
hour = time//3600
sec = (time % 3600)%60
print(f'{hour} часов {minute} минут {sec} секунд')
