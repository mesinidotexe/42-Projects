from parsing.parse import Parse
from colorama import init
import sys
    
# parameters = [nb_drones, (start_hub0 - start_hub1), start_hub_color, (end_hub0 - end_hub1), end_hub_color]
class Main():
    
    @classmethod
    def main(cls):
        # init(autoreset=True)
        # Parse.duplicate_line('nb_drones:')
        # Parse.duplicate_line('start_hub:')
        # Parse.duplicate_line('end_hub:')
            
        # if not Parse.first_line():
        #     sys.exit(1)
            
        
        # parameters: list[int | str | tuple[int | None, int | None] | None] | None = Parse.splitting_form_lines()
        # print(parameters)
        # if not parameters:
        #     print('Empty input_file, wrong input file name or invalid syntax')
        #     sys.exit(1)
        # if parameters is None or None in (parameters[0], parameters[1], parameters[3]):
        #     print('Invalid syntax in one or more lines on the first 3 lines in input_file, exitting the program')
        #     sys.exit(1)

        # if parameters[2] == 'outstandard':
        #     parameters[2] = '\x1b[0m'
        #     print('There is an outstandard color for "start_hub_color", the program will continue sticking with the regular terminal output color')
        # if parameters[4] == 'outstandard':
        #     parameters[4] = '\x1b[0m'
        #     print('There is an outstandard color for "end_hub_color", the program will continue sticking with the regular terminal output color')

        # hubs: list[dict[str, None| str, str | str, tuple[int, int]]] = Parse.hubs_positions()
        # for item in hubs:
        #     print(item)
        #     print()
        
        connections = Parse.get_connections()
        for item in connections:
            print(item)
        
    
    
    
if __name__ == '__main__':
    try:
        Main.main()
    except Exception as e:
        print(f'Failed dummy\n{e}')
