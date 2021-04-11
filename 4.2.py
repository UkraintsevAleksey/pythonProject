my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_new = my_list.copy()
my_list_new.pop(0)
new_list = []

for a, b in zip(my_list, my_list_new):
    if a < b:
       new_list.append(b)
print(new_list)



