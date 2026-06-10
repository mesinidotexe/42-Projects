from abc import ABC, abstractmethod
from ex0.ex0.creature import Flameling, Pyrodon
from ex0.ex0.creature import Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):

    def create_base(self):
        return Flameling('Flameling', 'fire')

    def create_evolved(self):
        return Pyrodon('Pyrodon', 'fire')


class AquaFactory(CreatureFactory):

    def create_base(self):
        return Aquabub('Aquabub', 'water')

    def create_evolved(self):
        return Torragon('Torragon', 'water')
