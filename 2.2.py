
element = 0
list = []
print('Нужно заполнить список элементами. Для окончания введите Stop')
while element != 'Stop':
    element = input('Ведите значение из списка ')
    list.append(element)
list.remove(element)
print(list)
j = 0
for i in range(int(len(list) / 2)):
    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2
print(list)


