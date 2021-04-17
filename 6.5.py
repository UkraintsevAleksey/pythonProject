class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Draw starting!")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Pen draw starting!")

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Pencil draw starting!")

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Handle draw starting!")


a = Stationary('Stationary')
a.draw()

a = Pen('Pen')
a.draw()

a = Pencil('Pencil')
a.draw()

a = Handle('Handle')
a.draw()