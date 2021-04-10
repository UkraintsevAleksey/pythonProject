def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Enter string instant of few words, using spacebar ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
