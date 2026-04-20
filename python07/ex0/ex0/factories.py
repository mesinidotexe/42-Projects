from .creature import Creature
from abc import ABC, abstractmethod

class Flameling(Creature):

    def __init__(self, name):
        self.name = name

    def attack(self):
        return f'{self.name} uses Ember!'
    

class Pyrodon(Creature):

    def __init__(self, name):
        self.name = name

    def attack(self):
        return f'{self.name} uses Flamethrower!'
    

class Aquabub(Creature):

    def __init__(self, name):
        self.name = name

    def attack(self):
        return f'{self.name} uses Water Gun!'
    

class Torragon(Creature):

    def __init__(self, name):
        self.name = name

    def attack(self):
        return f'{self.name} uses Hydro Pump!'
    

class CreatureFactory(ABC):

    @abstractmethod
    def create_base():
        pass
    
    @abstractmethod
    def create_evolved():
        pass