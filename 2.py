from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption # Что здесь происходит?

class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5 # Зачем делать округление? Это есть у условии задачи?

class Costume(Clothes):
    @property
    def consumption(self):
        return (2 * self.param + 0.3) / 100 # Зачем делить на 100? Это есть у условии задачи?

coat = Coat(58)
costume = Costume(240)
print(coat + costume)