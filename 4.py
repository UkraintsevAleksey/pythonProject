# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
a = input('Введите число ')
a = int(a)
max_figure: int = 0
while a > 0:
    last_figure = a % 10
    if last_figure > max_figure:
        max_figure = last_figure
    a = a / 10
print("Самая большая цифра = ", int(max_figure))