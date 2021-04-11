from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    print(el)

i=0
my_list = [1, 12, 1, 5, 6, 4, 7, 'fgd', 'fg', False]
for el in cycle(my_list):
    if i>20:
        break
    print(i, el)
    i += 1