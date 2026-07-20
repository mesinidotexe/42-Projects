from parse.parse import Parse
from colorama import init

def main():
    init(autoreset=True)
    parameters: list[int | str | tuple[int | None, int | None] | None] = Parse.splitting_fix()
    # parameters = [nb_drones, (start_hub0 - start_hub1), start_hub_color, (end_hub0 - end_hub1), end_hub_color]
    print(parameters)
    if None in 

if __name__ == '__main__':
    main()