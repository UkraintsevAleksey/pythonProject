def personal_inf(**kwargs):
    return ' '.join(kwargs.values())

name = input('Enter name - ')
surname = input('Enter surname - ')
birthday = input('Enter birthday - ')
city = input('Enter city - ')
email = input('Enter email - ')
phone = input('Enter phone - ')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))


