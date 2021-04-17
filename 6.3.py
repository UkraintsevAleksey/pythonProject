class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(int(self._income["wage"]) + int(self._income["bonus"]))


possition = Position('Tom', 'Cruse', 'Actor', 10000, 5000)

possition.get_full_name()
possition.get_total_income()