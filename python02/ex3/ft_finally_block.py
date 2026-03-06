def water_plants(plant_list):
    print("Opening Watering System\n\n")

    for plant in plant_list:
        try:
            int(plant)
            print(f"{plant} is not a valid name")
        except ValueError:
            print(f"Watering {plant}...")
        finally:
            try:
                int(plant)
            except ValueError:
                print(f"{plant} was sucefully watered\n")

def test_watering_system():
    plant_list = ["Rose,", "Tulip", "123"]
    water_plants(plant_list)

if __name__ == '__main__':
    test_watering_system()