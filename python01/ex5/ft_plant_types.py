class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        return self.bloom
        
class Tree(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        
    def produce_shade(self):
        return self.shade
        
class Vegetable(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        
    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin C")

        
def main():
    types = [
                Flower ('Rose', 25, 30, 'red'),
                Flower ('Violet', 15, 40, 'blue'),
                Tree ('Oak', 300, 1825, 50),
                Tree ('Palm', 800, 3765, ),
                Vegetable ('Tomato', 80, 90, 'summer harvest')
            ]

if __name__ == '__main__':
    main()