def generator(n):
    for el in range(1,n+1):
        yield el

n=int(input('Enter int for count factorial from 1 to int = '))
for el in range(1, n+1):
    fact = 1
    g = generator(el)
    for element in g:
        fact = fact * element
    print(f"{el}! = {fact}")
