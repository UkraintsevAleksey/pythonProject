class Organic_cell():

    def __init__(self, count):
        self.count_of_cells = count

    def __add__(self, other):
        return Organic_cell(self.count_of_cells + other.count_of_cells)

    def __sub__(self, other):
        if (self.count_of_cells - other.count_of_cells) > 0:
            return Organic_cell(self.count_of_cells - other.count_of_cells)
        else:
            print('Error! You can NOT subtract a quick cell from the first.')

    def __mul__(self, other):
        return Organic_cell(self.count_of_cells * other.count_of_cells)

    # def __truediv__(self, other):
    #    return Organic_cell(self.count // other.count)

    # def __str__(self):
    #    return f"Object cells = ({self.count})"

    def make_order(self, nums):
        return '\n'.join(['*' * nums for _ in range(self.count_of_cells) // nums]) + '\n' + '*' * (
                    self.count_of_cells % nums)

a = Organic_cell(5)
b = Organic_cell(12)
c = Organic_cell(a + b)
print(c.make_order(3))
