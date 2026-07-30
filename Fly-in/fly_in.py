from parsing.parse import Parse
from colorama import init
import sys
    
# start_end = [{'name', 'position', 'color'}, ...]  # start_hub then end_hub
class Main():
    
    @classmethod
    def main(cls):
        init(autoreset=True)
        Parse.duplicate_line('nb_drones:')
        Parse.duplicate_line('start_hub:')
        Parse.duplicate_line('end_hub:')
            
        if not Parse.first_line():
            sys.exit(1)
            
        nb_drones: int = Parse.get_nb_drones()
        print(f'nb_drones: {nb_drones}')
        
        start_end = Parse.splitting_form_lines()
        for item in start_end:
            print(item)
        print()

        if not start_end:
            print('Empty input_file, wrong input file name or invalid syntax')
            sys.exit(1)
        if len(start_end) < 2:
            print('Invalid syntax in one or more lines on the first 3 lines in input_file, exitting the program')
            sys.exit(1)

        if start_end[0]['color'] == 'outstandard':
            start_end[0]['color'] = '\x1b[0m'
            print('There is an outstandard color for "start_hub_color", the program will continue sticking with the regular terminal output color')
        if start_end[1]['color'] == 'outstandard':
            start_end[1]['color'] = '\x1b[0m'
            print('There is an outstandard color for "end_hub_color", the program will continue sticking with the regular terminal output color')

        hubs: list[dict[str, None| str, str | str, tuple[int, int]]] = Parse.hubs_positions()
        for item in hubs:
            print(item)
        
        print()
        
        connections = Parse.get_connections()
        for item in connections:
            print(item)
        
    
    
    
if __name__ == '__main__':
    try:
        Main.main()
    except Exception as e:
        print(f'Failed dummy\n{e}')
