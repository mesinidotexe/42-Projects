from colorama import Fore
import re
import sys

class ZoneError(Exception):
    pass

class Parse():
    
    standard_zones: list[str] = ['normal', 'blocked', 'restricted', 'priority']
    
    # Auxiliar method
    @staticmethod
    def metadata(line: str) -> bool:
        return '[' in line or ']' in line

    # Auxiliar method
    @staticmethod
    def get_color(line: str) -> str | None:
        colors = {
            'black': Fore.BLACK,
            'blue': Fore.BLUE,
            'cyan': Fore.CYAN,
            'green': Fore.GREEN,
            'magenta': Fore.MAGENTA,
            'red': Fore.RED,
            'white': Fore.WHITE,
            'yellow': Fore.YELLOW,
            'gray': Fore.LIGHTBLACK_EX
        }
        metadata = line.split('[')[1].split(']')[0]
        match = re.search(r'color=(\w+)', metadata)
        if not match:
            return None

        color_name = match.group(1)
        if color_name not in colors:
            return 'outstandard'

        return colors[color_name]
    
    
    # Auxiliar method
    @staticmethod
    def bracket_validator(s: str) -> bool:
        stack: list = []
        pairs: dict[str] = {
            ']': '['
            }

        for char in s:
            if char in '[':
                stack.append(char)

            elif char in ']':
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return len(stack) == 0

    @classmethod
    def duplicate_line(cls, phrase: str) -> bool:
        counter: int = 0
        with open('input_file.txt') as input_file:
            for line in input_file:
                if line.startswith(phrase):
                    counter += 1
        if counter > 1:
            return False
        return True
                
    @classmethod
    def first_line(cls):
        with open('input_file.txt') as input_file:
            if not input_file.readlines()[0].startswith('nb_drones:'):
                    print('The first line should start with "nb_drones:"')
                    return False
            return True

    @classmethod
    def splitting_fix_lines(cls) -> list:
        variables: list[int | str | None | tuple] = []

        with open('input_file.txt') as input_file:
            for line in input_file:

                if line.startswith('nb_drones:'):
                    try:
                        number_of_drones: int | None = (int(line.split(':')[1]) if len(line.split(':')) == 2 else None)
                        if number_of_drones <= 0:
                            print('Number of dones must be 1 or higher')
                            return None
                        variables.append(number_of_drones)
                    except ValueError:
                        print('The amount of drones must be an integer')
                        return None

                elif line.startswith('start_hub:'):
                    start_parts: list = line.split()
                    if len(start_parts) in (4, 5):
                        try:
                            x = int(start_parts[2])
                            y = int(start_parts[3])
                            if x < 0 or y < 0:
                                print('Position must be positive')
                                return None
                            start_hub: tuple[int, int] = (x, y)
                            variables.append(start_hub)
                        except ValueError:
                            print('Invalid syntax on line "start_hub", args 2 and 3 must be an integer')
                            return None
                    else:
                        print('Invalid syntax on line "start_hub"')
                        return None

                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            print('Invalid input file on first 3 parameters, maybe you forgot to close the "[]"?')
                            return None
                        start_hub_color = cls.get_color(line)
                        variables.append(start_hub_color)
                    else:
                        variables.append(None)

                elif line.startswith('end_hub:'):
                    end_parts: list = line.split()
                    if len(end_parts) in (4, 5):
                        try:
                            x = int(end_parts[2])
                            y = int(end_parts[3])
                            if x < 0 or y < 0:
                                print('Position must be positive')
                                return None
                            end_hub: tuple[int, int] = (x, y)
                            variables.append(end_hub)
                        except ValueError:
                            print('Invalid syntax on line "end_hub", args 2 and 3 must be an integer')
                            return None
                    else:
                        print('Invalid syntax on line "end_hub"')
                        return None

                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            print('Invalid input file, maybe you forgot to close the "[]"?')
                            return None
                        end_hub_color = cls.get_color(line)
                        variables.append(end_hub_color)
                    else:
                        variables.append(None)
                
        return variables
    
    #auxiliar method
    @staticmethod
    def parse_metadata(line: str) -> dict:
        if '[' not in line:
            return {}

        meta_str = line.split('[')[1].split(']')[0]
        metadata: dict[str, str] = {}
        for pair in meta_str.split():
            key, value = pair.split('=')
            metadata[key] = value

        return metadata
    
    #auxiliar method
    @staticmethod
    def check_valid_name(line: str) -> bool:
        try:
            splitted: list = line.split()
            if not line.startswith('connection') and '-' in splitted[1] or ' ' in splitted[1]:
                return False
            return True
        except IndexError:
            return True
        
    @classmethod
    def hubs_positions(cls) -> list[dict] | None:
        data: list = []
        
        with open('input_file.txt') as input_file:
            for line in input_file:
                
                if not line.startswith('nb_drones:') and not cls.check_valid_name(line):
                    print('Invalid hub name (cannot have "-")')
                    return None
                
                if line.startswith('hub:'):
                    parts = line.split()
                    key = parts[1]
                    try:
                        value = (int(parts[2]), int(parts[3]))
                        if value[0] < 0 or value[1] < 0:
                            print('Hub position must be positive')
                            return None
                    except Exception:
                        print('You must pass an integer on aruments 2 and 3 of hubs')
                        return None
                    
                    hub_entry = {'name': key, 'position': (value)}
                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            print('Invalid input file on hubs, maybe you forgot to close the "[]"?')
                            return None

                        standard_zones: list[str] = [None, 'normal', 'blocked', 'restricted', 'priority']
                        metadata: dict = cls.parse_metadata(line)
                        if metadata.get('zone') in standard_zones: 
                            hub_entry['zone'] = metadata.get('zone')
                            if hub_entry['zone'] is None:
                                hub_entry['zone'] = 'normal'
                        else:
                            raise ZoneError('Zone name not in the standards')
                            
                        hub_entry['color'] = cls.get_color(line)
                        if hub_entry['color'] is None or hub_entry['color'] == 'outstandard':
                            hub_entry['color'] = '\x1b[0m'
                        
                        try:
                            hub_entry['max_drones'] = int(metadata.get('max_drones')) if metadata.get('max_drones') is not None else 1
                            if metadata.get('max_drones') is not None and int(metadata.get('max_drones')) < 0:
                                print('max_drones field must be a positive integer')
                                return None
                        except ValueError:
                            print('A positive integer must be passed as a parameter')
                            return None
                        data.append(hub_entry)
        return data
    
    
    # @classmethod
    # def connections(cls) -> str:
        