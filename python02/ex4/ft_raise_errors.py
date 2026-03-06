class EmptyError(Exception):
    pass

class WaterError(Exception):
    pass

class LightError(Exception):
    pass

def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name == "":
            raise EmptyError("The name of the plant cannot be empty!")
        if water_level < 1 or water_level > 10:
            raise WaterError("Wrong amount of water!")
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise LightError("Not the ideal time of sunlight!")
    finally:
        print()


def test_plant_checks():
    tests = [
        ("Rose", 5, 5),
        ("", 5, 5),
        ("Rose", 0, 5),
        ("Rose", 5, 0)
    ]

    for plant, water, sun in tests:
        try:
            check_plant_health(plant, water, sun)
            print("Plant is healthy")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    test_plant_checks()