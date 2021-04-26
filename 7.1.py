a = [[3, 1, 6], [4, 4, 5], [0, 5, 0]]
b = [[1, 1, 6], [2, 9, 2], [8, 3, 5]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        b = []
        for i in range(len(self.lists)):
            b.append([])
            for j in range(len(self.lists[0])):
                b[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, b))

matrx1 = Matrix(a)
matrx2 = Matrix(b)

print(matrx1, '\n')
print(matrx2, '\n')
print(matrx1 + matrx2)