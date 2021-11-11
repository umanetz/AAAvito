import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):

    @property
    @abstractmethod
    def exp(self):
        pass

    @abstractmethod
    def inc_exp(self, val):
        pass

    def __str__(self):
        pass


class Pokemon(AnimeMon):

    def __init__(self, name):
        self.name = name
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value):
        self._exp += value

    def __str__(self):
        return self.name


class Digimon(AnimeMon):

    def __init__(self, name):
        self.name = name
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value):
        self._exp += value * 8

    def __str__(self):
        return self.name


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur')
    agumon = Digimon(name='Agumon')

    train(bulbasaur)
    print(f'{bulbasaur}: {bulbasaur.exp}')

    train(agumon)
    print(f'{agumon}: {agumon.exp}')

