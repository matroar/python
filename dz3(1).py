def result (x, y):
   try:
       return (x / y)
   except ZeroDivisionError:
       return ('Недопустимое значение y')
x = int(input('Введите x: '))
y = int(input('Введите y: '))
print(result(x, y))
