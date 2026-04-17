from .elements import create_air
from .potions import healing_potion, strength_potion
from alchemy.transmutation.recipes import lead_to_gold

def heal():
    return healing_potion()