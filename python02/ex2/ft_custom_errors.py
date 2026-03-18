class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_garden(name):
    try:
        int(name)
        raise GardenError("Garden name cannot be a number")
    except ValueError:
        pass


def check_plant(plant):
    if plant != "flower":
        raise PlantError("This is not a flower")


def check_water(liters):
    try:
        liters = int(liters)
    except ValueError:
        raise WaterError("Water must be a number")

    if liters < 0:
        raise WaterError("Liters cannot be negative")


def main():
    name = input("Enter your Garden name: ")
    plant = input("Enter your Plant name: ")
    liters = input("Enter the liters watered: ")

    try:
        check_garden(name)
        check_plant(plant)
        check_water(liters)
        print("Garden setup is valid")

    except GardenError as e:
        print(e)


if __name__ == '__main__':
    main()
