list = [7,5,3,3,2]
new_element = input('Введите новый элемент рейтинга ')
list.append(int(new_element))
list.sort(reverse=True)
print(list)
