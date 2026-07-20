from colorama import Fore
import re

class Parse():
    
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
        match = re.search(r'color=(\w+)', line)
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
    def splitting_fix_lines(cls) -> list:
        variables: list[int | str | None | tuple] = []

        with open('input_file.txt') as input_file:
            for line in input_file:

                if line.startswith('nb_drones'):
                    try:
                        number_of_drones: int | None = (int(line.split(':')[1]) if len(line.split(':')) == 2 else None)
                        variables.append(number_of_drones)
                    except ValueError:
                        print('The amount of drones must be an integer')
                        return None

                elif line.startswith('start_hub'):
                    start_parts: list = line.split()
                    if len(start_parts) in (4, 5):
                        try:
                            x = int(start_parts[2])
                            y = int(start_parts[3])
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
                            print('Invalid input file, maybe you forgot to close the "[]"?')
                            return None
                        start_hub_color = cls.get_color(line)
                        variables.append(start_hub_color)
                    else:
                        variables.append(None)

                elif line.startswith('end_hub'):
                    end_parts: list = line.split()
                    if len(end_parts) in (4, 5):
                        try:
                            x = int(end_parts[2])
                            y = int(end_parts[3])
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
    
    @classmethod
    def hubs_positions(cls):
        hubs: dict[str, tuple[int, int]] = {}
        with open('input_file.txt') as input_file:
            for line in input_file:
                if line.startswith('hub'):
                    parts = line.split()
                    key = parts[1]
                    try:
                        value = int(parts[2], int(parts[3]))
                    except ValueError:
                        print('You must pass an integer as a position')
                        return None
                    