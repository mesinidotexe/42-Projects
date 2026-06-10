import math


def get_player_pos():
    while True:
        try:
            x = float(input("Enter a valid value for 'x': "))
            y = float(input("Enter a valid value for 'y': "))
            z = float(input("Enter a valid value for 'z': "))
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter coordinates in format x,y,z")


def distance_3d(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main():
    print("=== Game Coordinate System ===")

    pos1 = (get_player_pos())

    print("Position tuple:", pos1)
    print("x:", pos1[0])
    print("y:", pos1[1])
    print("z:", pos1[2])

    center = (0, 0, 0)
    dist_center = distance_3d(pos1, center)
    print("Distance to center:", round(dist_center, 2))

    pos2 = (get_player_pos())

    dist_between = distance_3d(pos1, pos2)
    print("Distance between points:", round(dist_between, 2))


if __name__ == "__main__":
    main()
