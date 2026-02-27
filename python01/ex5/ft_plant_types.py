class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show_info(self):
        print(f"{self.name} ({self.__class__.__name__}): "
              f"{self.height} cm, {self.age} days")
        
        
class Flower(Plant):
    def __init__(self, name, height, age, color: str):
        super().__init__(name, height, age)
        self.color = color
        
    def bloom(self):
        if self.height > 20:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} did not grow much this season")

    def show_info(self):
        super().show_info()
        print(f"Has the {self.color} color")
        self.bloom()

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        
    def produce_shade(self):
        print(f"{self.name} has {self.trunk_diameter}cm diameter and"
              f" provides {self.trunk_diameter / 100 * self.height}"
              f" square meters of shade")

    def show_info(self):
        super().show_info()
        self.produce_shade()
        
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str, vitamin: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.vitamin = vitamin
        
    def nutritional_value(self):
        print(f"{self.name} is from {self.harvest_season} and is rich in {self.vitamin}")
        
    def show_info(self):
        super().show_info()
        self.nutritional_value()

        
def main():
    types = [
                Flower('Rose', 25, 30, 'Red'),
                Flower('Violet', 15, 40, 'Blue'),
                Tree('Oak', 300, 1825, 50),
                Tree('Palm', 800, 3765, 35),
                Vegetable('Tomato', 80, 90, 'summer harvest', 'vitamin c'),
                Vegetable('Onion', 45, 90, 'winter harvest', 'tears')
            ]
    
    for plant in types:
        plant.show_info()
        print()

if __name__ == '__main__':
    main()
