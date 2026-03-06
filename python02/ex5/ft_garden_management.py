class EmptyError(Exception):
    pass

class WaterError(Exception):
    pass

class LightError(Exception):
    pass


class GardenManager:

    def __init__(self):
        self.gardens = []
    
    def add_plant(self, name, water, light):
        if name == "":
            raise EmptyError("The name of the plant cannot be empty!")
        self.gardens = {"water": water, "light": light}

    def water_plant(self, water):
        if water < 1 or water > 10:
            raise WaterError("Wrong amount of water!")

    def check_plant_health(self, light):
        if light < 2 or light > 12:
            raise LightError("Not the ideal time of sunlight!")

    def errors_type(self):
        try:
            self.add_plant()
        except Exception as e:
            print(e)


def test_garden_management():
    manager = GardenManager()

    # adicionar plantas
    manager.add_plant("Rose", 5, 5)
    manager.add_plant("", 5, 5)  # erro

    # regar plantas
    manager.water_plant(5)
    manager.water_plant(-1)  # erro

    # checar saúde
    manager.check_health("5")
    manager.check_health("1")  # erro

if __name__ == '__main__':
    test_garden_management()