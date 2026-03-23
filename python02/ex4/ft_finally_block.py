class PlantError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name):
    if not plant_name[0].isupper():
        raise PlantError(f"Plant name '{plant_name}'"
                         f"must start with a capital letter")

    print(f"Watering plant: {plant_name}")


def test_watering_system():
    plants = ["Rose", "tulip", "Sunflower"]

    print("Opening watering system...\n")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Error: {e}")
        print("Stopping watering process...\n")
        return
    finally:
        print("Closing watering system... (cleanup always runs)")

    print("\nAll plants watered successfully!")


if __name__ == '__main__':
    test_watering_system()
