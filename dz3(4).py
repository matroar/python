def my_func (x, y):
    return x**y
print(my_func(12, -3))

def my_func_2 (x, y):
    n = 1
    x_const = x
    while n < abs(y):
        x = x * x_const
        n += 1
    return 1/x

print (my_func_2(12, -3))