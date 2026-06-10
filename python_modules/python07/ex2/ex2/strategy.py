from abc import ABC, abstractmethod
# from ex1.ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature):
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if creature is not None:
            return True
        return False

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception('invalid Creature for this aggressive strategy')
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, 'transform')

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception('invalid Creature for this aggressive strategy')
        return (
            creature.attack() + '\n' +
            creature.transform() + '\n' +
            creature.transformed_attack() + '\n' +
            creature.revert()
            )


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, 'heal')

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception('invalid Creature for this aggressive strategy')
        return (
            creature.attack() + '\n' +
            creature.heal()
        )
