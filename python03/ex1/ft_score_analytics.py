import sys

def main(argv):
	count = 0
	for arg in argv[1:]:
		count += 1
	if count == 0:
		print('No scores provided')
	else:
		try:
			i = 1
			lista = []
			for arg in argv[1:]:
				lista.append(int(argv[i]))
				i += 1
		except ValueError:
			print('Non integer value provided, please enter value again!')
			return
		print(f'Total players: {len(lista)}')
		print(f'Total Score: {sum(lista)}')
		print(f'Average score: {sum(lista) / len(lista)}')
		print(f'Highest Score: {max(lista)}')
		print(f'Lowest score: {min(lista)}')
		print(f'Score Range: {max(lista) / min(lista)}')

if __name__ == '__main__':
	main(sys.argv)