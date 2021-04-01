# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
current_time = input('Введите текущее время в секундах ')
current_time = int(current_time)
hour: float = current_time / 3600
current_time = current_time - int(hour) * 3600
minute = current_time / 60
second = current_time - int(minute) * 60
if hour > 24:
    hour = hour % 24
print(f'{round(int(hour),2)}:{round(int(minute),2)}:{round(second,2)}')
