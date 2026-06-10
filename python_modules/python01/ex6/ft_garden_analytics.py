class Garden:
    """Represents a garden owned by a single person."""

    def __init__(self, owner):
        """Create a new garden for the given owner."""
        self.owner = owner
        self.plants = []


class Plant:
    """Basic plant with a name, type, and height."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def describe(self):
        print(f"- {self.name}\n\t-> Height: {self.height}cm, "
              f"{self.age} days old")


class FloweringPlant(Plant):
    """A plant that has flowers and color"""
    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age)
        self.flower_color = flower_color

    def describe(self):
        super().describe()
        print(f"\t-> Color: {self.flower_color}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color, prize_year):
        super().__init__(name, height, age, flower_color)
        self.prize_year = prize_year

    def describe(self):
        super().describe()
        print(f"\t-> Prize Year: {self.prize_year}")


class GardenManager:
    """Manages multiple gardens and generates reports."""

    total_gardens = 0

    def __init__(self):
        self.gardens = []  # lista de jardins de cada manager

    def creat_garden_network(self, garden):
        self.gardens = self.gardens + [garden]
        GardenManager.total_gardens += 1  # incrementa contador global

    @classmethod
    def count_gardens(cls):
        """Retorna a quantidade total de jardins criados"""
        return cls.total_gardens

    class GardenStats:
        """Calculates and stores statistics for a garden."""
        def __init__(self, garden):
            self.garden = []

        def showname(self):
            print(self.owner)


def main():
    print("=== Garden Management System Demo ===\n")
    manager1 = GardenManager()

    garden_a = Garden("Alice")
    garden_b = Garden("Bob")
    garden_c = Garden("Seu Ze")

    cactus = Plant("Cactus", 69, 28)
    rose = FloweringPlant("Rose", 15, 40, "Red")
    orchhid = PrizeFlower("Orchid", 28, 60, "White", 2026)

    GardenManager.GardenStats.showname(garden_a)
    Plant.describe(cactus)
    GardenManager.GardenStats.showname(garden_b)
    FloweringPlant.describe(rose)
    GardenManager.GardenStats.showname(garden_c)
    PrizeFlower.describe(orchhid)

    manager1.creat_garden_network(garden_a)
    manager1.creat_garden_network(garden_b)
    manager1.creat_garden_network(garden_c)

    print("Total gardens:", GardenManager.count_gardens())


if __name__ == '__main__':
    main()
