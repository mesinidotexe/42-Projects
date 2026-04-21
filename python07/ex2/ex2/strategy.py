from abc import ABC, abstractmethod
from ex1.ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self):
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if creature is not None:
            return True

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception('invalid Creature for this aggressive strategy')
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception('invalid Creature for this aggressive strategy')
        return creature.attack()


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception('invalid Creature for this aggressive strategy')
        return creature.attack()
