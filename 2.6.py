print('Необходимо будет ввести 3 записи о товарах ')
list = []
for ind in range(1, 3):
    name = input('Введите название товара ')
    price = input('Введите цену товара ')
    count = input('Введите кол-во товара ')
    ei = input('Введите единицу измерения товара ')
    my_dict1 = {"название":name,"цена":price, "количество":count,"ед.":ei}
    my_tuple1 = (ind, my_dict1)
    # список кортежей, часть 1 задания
    list.append(my_tuple1)
print(list)






