def my_sum ():
    sum_res = 0
    stop = ' '
    while stop != '*':
        number = input('Введите числа через пробел или * для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == '*' :
                stop = '*'
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел:  {sum_res}')
    print(f'Итоговая сумма:  {sum_res}')


my_sum()