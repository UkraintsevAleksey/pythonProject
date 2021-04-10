num = 0
try:
    while num != 'q':
        for i in map(int, input("For exit press 'q' Enter figures, using spacebar - ").split()):
            num += i
        print(num)
except ValueError:
    print(num)