class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self):
        self.height += 1
        self.age += 1
        self.growth += 1


def main():
    plants = [
              Plant('Rose', 25, 30),
              Plant('Sunflower', 80, 45),
              Plant('Cactus', 15, 120)
             ]

    day = 1
    while day < 8:
        if day in (1, 7):
            print(f"=== Day {day} ===")
            for plant in plants:
                print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
        for plant in plants:
            plant.grow()
        day += 1

    print(f"Growth this week: +{day - 2}cm")


if __name__ == '__main__':
    main()
