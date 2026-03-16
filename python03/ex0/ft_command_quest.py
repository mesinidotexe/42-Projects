import sys

def main(argv):
	print("=== Command Quest ===")
	i = 0
	for arg in argv:
		i += 1
	if i == 1:
		print("No arguments provided!")
		print(f"Program Name = {argv[0]}")
	else:
		count = 1
		print(f"Arguments recieved: {i - 1}")
		for j in argv[1:]:
			print(f'Argument {count}: {j}')
			count += 1
	print(f'Total arguments: {len(sys.argv)}')


if __name__ == '__main__':
	main(sys.argv)
