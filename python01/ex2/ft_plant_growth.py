class Plant:
    def __init__(self, name: str, height: int, old: int):
        self.name = name
        self.height = height
        self.old = old
        self.growth = 0

    def grow(self):
        self.height += 1
        self.growth += 1

    def age(self):
        self.old += 1

    def get_info():
        print("It grew beatifully!")

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
                print(f"{plant.name}: {plant.height}cm, {plant.old} days old")
        for plant in plants:
            plant.grow()
            plant.age()
        day += 1

    print(f"Growth this week: +{day - 2}cm")
    Plant.get_info()


if __name__ == '__main__':
    main()
