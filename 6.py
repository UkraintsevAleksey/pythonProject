#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
result = input('Введите сколько км спортсмен пробежал в 1 день: ')
total_result = input('Введите сколько км спортсмен должен пробежать? ')
result = int(result)
i = 0
while result <= int(total_result):
    i += 1
    print(f'{i} день: {round(result,2)} км')
    result *= 1.1
i += 1
print(f'{i} день: {round(result,2)} км')
result *= 1.1
print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {total_result} км.')