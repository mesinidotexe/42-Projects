import sys
import math

def main(argv):
    print('=== Game Coordinate System ===')
    i = 0
    for arg in argv:
        i += 1
    if i >= 4:
        try:
            x = int(argv[1])
            y = int(argv[2])
            z = int(argv[3])
        except ValueError:
            raise ValueError('Non integer value passed as a parameter')
        except IndexError:
            print("Please provide 3 coordinates")
            return
        coord = (x, y, z)
        print(f'Parsing coordinates: {coord}')
        print(f'Parsed position: {coord}')
        distance = math.sqrt((x - 0)** 2 + (y - 0)** 2 + (z - 0)** 2)
        print(f'Distance between (0, 0, 0) and {coord}: {float(distance)}')
    elif i == 2:
        args = argv[1].split()
        try:
            x = int(args[0])
            y = int(args[1])
            z = int(args[2])
        except ValueError:
            raise ValueError('Non integer value passed as a parameter')
            
        distance = math.sqrt((x - 0)** 2 + (y - 0)** 2 + (z - 0)** 2)
        print(f'Distance between (0, 0, 0) and {args}: {float(distance)}')
if __name__ == '__main__':
    main(sys.argv)
