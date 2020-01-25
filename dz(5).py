revenue = int(input('Введите выручку фирмы: '))
cost = int(input('Введите издержки фирмы: '))
profit = revenue - cost
profitability = profit / revenue * 100
if revenue > cost:
    print('Фирма работает с прибылью. Рентабельность ', profitability, ' %')
elif revenue == cost:
    print('Выручка равна издержкам')
else:
    print('Фирма работает с убытком')