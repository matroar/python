my_list = [1, 6, 6, 2, 3, 2, 8, 19, 5, 8]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)