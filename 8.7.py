class Complex_Number:
    def __init__(self, a, j):
        self.a = a
        self.j = j

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'c = {self.a + other.a} + {self.j + other.j} * j'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'c = {self.a * other.a - (self.j * other.j)} + {self.j * other.a} * j'


c_1 = Complex_Number(1, -2)
c_2 = Complex_Number(3, 4)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)