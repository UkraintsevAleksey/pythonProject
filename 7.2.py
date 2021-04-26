from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        if self.param > 0:
            return round(self.param / 6.5) + 0.5
        else:
            print('Error! Invalid size of coat, must be > 0!')


class Suit(Clothes):
    @property
    def consumption(self):
        if self.param>0:
            return (2 * self.param + 0.3) / 100
        else:
            print('Error! Invalid size of suit, must be > 0 !')

coat = Coat(92)
suit = Suit(122)
print(coat + suit)