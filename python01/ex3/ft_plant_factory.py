class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

def main():
	tipo = [
		      Plant ('Rose', 25, 30),
		   	  Plant ('Oak', 200, 365),
			  Plant ('Cactus', 5, 90),
			  Plant ('Sunflower', 80, 45),
			  Plant ('Fern', 15, 120)
		     ]
	print ("=== Plant Factory Output ===")
	i = 0
	for plant in tipo:
		print(f"Created: {plant.name}({plant.height}cm, {plant.age} days)")
		i += 1
	print(f"Total plants created: {i}")

if __name__ == '__main__':
	main()