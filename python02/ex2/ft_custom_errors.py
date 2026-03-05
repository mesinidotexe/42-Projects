class GardenError(Exception):
	print("The type for the garden is not valid")


class PlantError(Exception):
	print("This is not a flower")


class WaterError(Exception):
	print("The amount of liters is under the es")

def main(name, plant, liters):
	try:
		GardenError()
	except:

if __name__ == '__main__':
	main("Alice", "Rose", 30)