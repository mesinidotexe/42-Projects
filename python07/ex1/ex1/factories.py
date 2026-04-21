from .capabilities import Sproutling, Bloomelle
from .capabilities import Shiftling, Morphagon
from ex0.ex0.factories import CreatureFactory

class HealingCreatureFactory(CreatureFactory):

    def create_base(self):
        return Sproutling('Sproutling', 'grass')

    def create_evolved(self):
        return Bloomelle('Bloomelle', 'grass/fairy')


class TransformCreatureFactory(CreatureFactory):

    def create_base(self):
        return Shiftling('Shiftling', 'normal')
    
    def create_evolved(self):
        return Morphagon('Morphagon', 'normal/dragon')