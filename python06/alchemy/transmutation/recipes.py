from ..elements import create_air, create_earth
from elements import create_fire
import alchemy.potions

def lead_to_gold():
    return (f'Recipe transmuting Lead to Gold: brew {create_air()} and {alchemy.potions.strength_potion()} mixed with {create_fire()}')