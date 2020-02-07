my_list = [44, 8, 3, 27, 11, 8, 5, 1]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Новый список {my_new_list}')