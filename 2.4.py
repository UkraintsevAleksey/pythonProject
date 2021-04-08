text = input('Введите строк из нескольких слов, разделенных пробелами ')
text = text.split()
for ind, el in enumerate(text, 1):
    print(ind, el[0:10])