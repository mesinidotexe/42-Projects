class EmptyError(Exception):
    pass

class WaterError(Exception):
    pass

class LightError(Exception):
    pass


class GardenManager:

    def __init__(self):
        self.gardens = {}
    
    def add_plant(self, name, water, light):
        if name == "":
            raise EmptyError("The name of the plant cannot be empty!")
        self.gardens[name] = {"water": water, "light": light}
        print(f"{name} added!")


    def water_plant(self, name, water):
        print("Opening watering sysytem")
        try:
            if water < 1 or water > 10:
                raise WaterError(f"Wrong amount of water for {name}!")
            print(f"Watering {name} with {water} liters")
        finally:
            print("Closing watering system\n")


    def check_plant_health(self, name):
        plant = self.gardens.get(name)

        if not plant:
            raise EmptyError(f"{name} is not in the garden")

        light = plant["light"]

        if light < 2 or light > 12:
            raise LightError(f"{name} is not getting ideal sunlight")

        print(f"{name} is healthy")


def test_garden_management():
    manager = GardenManager()

    # adicionar plantas
    manager.add_plant("Rose", 5, 5)
    manager.add_plant("Tulip", 5, -1)
    try:
        manager.add_plant("", 5, 5)  # erro
    except EmptyError as e:
        print(f"{e}\n")


    # regar plantas
    manager.water_plant("Rose", 5)
    manager.water_plant("Tulip", 5)
    try:
        manager.water_plant("Tulip", -1)  # erro
    except WaterError as e:
        print(f"{e}\n")

    # checar saúde
    manager.check_plant_health("Rose")
    try:
        manager.check_plant_health("Tulip")  # erro
    except LightError as e:
        print(e)

if __name__ == '__main__':
    test_garden_management()