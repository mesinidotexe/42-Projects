from colorama import Fore
import re
import parsing.exceptions as exceptions

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
    def duplicate_line(cls, phrase: str) -> None:
        lines_found: list[int] = []
        with open('input_file.txt') as input_file:
            for line_num, line in enumerate(input_file, start=1):
                if line.startswith(phrase):
                    lines_found.append(line_num)
        if len(lines_found) > 1:
            label = phrase.rstrip(':')
            raise exceptions.InvalidSyntaxError(
                f'Duplicate "{label}" entries at lines {", ".join(map(str, lines_found))}'
            )
                
    @classmethod
    def first_line(cls):
        with open('input_file.txt') as input_file:
            if not input_file.readlines()[0].startswith('nb_drones:'):
                    print('The first line should start with "nb_drones:"')
                    return False
            return True

    @classmethod
    def get_nb_drones(cls) -> int:
        with open('input_file.txt') as input_file:
            for line_num, line in enumerate(input_file, start=1):

                if line.startswith('nb_drones:'):
                    raw_nb = line.split(':', 1)[1].strip() if len(line.split(':', 1)) == 2 else ''
                    try:
                        number_of_drones: int | None = (int(raw_nb) if len(line.split(':')) == 2 else None)
                        if number_of_drones <= 0:
                            raise exceptions.NegativeError(f'line {line_num}: nb_drones must be >= 1, got {number_of_drones}')

                        return number_of_drones
                    except ValueError:
                        raise exceptions.NotIntError(f'line {line_num}: nb_drones must be an integer, got "{raw_nb}"')

    @classmethod
    def splitting_form_lines(cls) -> list[dict]:
        result: list[dict] = []

        with open('input_file.txt') as input_file:
            for line_num, line in enumerate(input_file, start=1):
                if line.startswith('start_hub:'):
                    start_parts: list = line.split()
                    if len(start_parts) in (4, 5, 6):
                        try:
                            name = start_parts[1]
                            x = int(start_parts[2])
                            y = int(start_parts[3])
                            if x < 0 or y < 0:
                                raise exceptions.NegativePositionError(
                                    f'line {line_num}: start_hub position must be >= 0, got ({x}, {y})'
                                )
                            start_hub: dict = {
                                'name': name,
                                'position': (x, y),
                                'color': None,
                            }
                        except ValueError:
                            raise exceptions.NotIntPositionError(
                                f'line {line_num}: start_hub x/y must be integers, got "{start_parts[2]}" "{start_parts[3]}"'
                            )
                    else:
                        raise exceptions.InvalidSyntaxError(
                            f'line {line_num}: start_hub expects: name x y [metadata], got {len(start_parts)} tokens: {start_parts}'
                        )

                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            raise exceptions.OpenBracketError(
                                f'line {line_num}: Unclosed brackets in metadata: "{line.strip()}"'
                            )

                        metadata = cls.parse_metadata(line, line_num)
                        allowed = {'color', 'max_drones'}
                        unknown = set(metadata) - allowed
                        if unknown:
                            raise exceptions.InvalidSyntaxError(
                                f'line {line_num}: Unknown metadata key(s) on start_hub: {", ".join(unknown)}'
                            )

                        start_hub['color'] = cls.get_color(line)

                    result.append(start_hub)

                elif line.startswith('end_hub:'):
                    end_parts: list = line.split()
                    if len(end_parts) in (4, 5, 6):
                        try:
                            name = end_parts[1]
                            x = int(end_parts[2])
                            y = int(end_parts[3])
                            if x < 0 or y < 0:
                                raise exceptions.NegativePositionError(
                                    f'line {line_num}: end_hub position must be >= 0, got ({x}, {y})'
                                )
                            end_hub: dict = {
                                'name': name,
                                'position': (x, y),
                                'color': None,
                            }
                        except ValueError:
                            raise exceptions.NotIntPositionError(
                                f'line {line_num}: end_hub x/y must be integers, got "{end_parts[2]}" "{end_parts[3]}"'
                            )
                    else:
                        raise exceptions.InvalidSyntaxError(
                            f'line {line_num}: end_hub expects: name x y [metadata], got {len(end_parts)} tokens: {end_parts}'
                        )

                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            raise exceptions.OpenBracketError(
                                f'line {line_num}: Unclosed brackets in metadata: "{line.strip()}"'
                            )

                        metadata = cls.parse_metadata(line, line_num)
                        allowed = {'color', 'max_drones'}
                        unknown = set(metadata) - allowed
                        if unknown:
                            raise exceptions.InvalidSyntaxError(
                                f'line {line_num}: Unknown metadata key(s) on end_hub: {", ".join(unknown)}'
                            )

                        end_hub['color'] = cls.get_color(line)

                    result.append(end_hub)

        return result
    
    #auxiliar method
    @staticmethod
    def parse_metadata(line: str, line_num: int | None = None) -> dict:
        if '[' not in line:
            return {}

        prefix = f'line {line_num}: ' if line_num is not None else ''
        meta_str: str = line.split('[')[1].split(']')[0]
        metadata: dict[str, str] = {}
        for pair in meta_str.split():
            if '=' not in pair:
                raise exceptions.InvalidSyntaxError(
                    f'{prefix}Invalid metadata token "{pair}" (expected key=value)'
                )
            key, value = pair.split('=', 1)
            if not key or not value:
                raise exceptions.InvalidSyntaxError(
                    f'{prefix}Invalid metadata token "{pair}" (expected key=value)'
                )
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
        
    @staticmethod
    def doubled_name(data: list[dict]) -> bool:
        seen: list[str] = []
        for item in data:
            if item.get('name') in seen:
                return True
            seen.append(item.get('name')) 
        return False
        
    @classmethod
    def hubs_positions(cls) -> list[dict]:
        data: list[dict] = []
        
        with open('input_file.txt') as input_file:
            for line_num, line in enumerate(input_file, start=1):
                
                if not line.startswith('nb_drones:') and not cls.check_valid_name(line):
                    name = line.split()[1] if len(line.split()) > 1 else '?'
                    raise exceptions.DashInNameError(
                        f'line {line_num}: Hub name cannot contain "-", got "{name}"'
                    )
                
                if line.startswith('hub:'):
                    parts = line.split()
                    key = parts[1]
                    try:
                        value = (int(parts[2]), int(parts[3]))
                        if value[0] < 0 or value[1] < 0:
                            raise exceptions.NegativeHubPositionError(
                                f'line {line_num}: hub "{key}" position must be >= 0, got {value}'
                            )
                    except exceptions.NegativeHubPositionError:
                        raise
                    except (ValueError, IndexError):
                        x_token = parts[2] if len(parts) > 2 else '<missing>'
                        y_token = parts[3] if len(parts) > 3 else '<missing>'
                        raise exceptions.NotIntPositionError(
                            f'line {line_num}: hub "{key}" x/y must be integers, got "{x_token}" "{y_token}"'
                        )
                    
                    hub_info = {'name': key, 'position': (value)}
                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            raise exceptions.OpenBracketError(
                                f'line {line_num}: Unclosed brackets in metadata: "{line.strip()}"'
                            )

                        standard_zones: list[None | str] = [None, 'normal', 'blocked', 'restricted', 'priority']
                        metadata: dict = cls.parse_metadata(line, line_num)
                        if metadata.get('zone') in standard_zones: 
                            hub_info['zone'] = metadata.get('zone')
                            if hub_info['zone'] is None:
                                hub_info['zone'] = 'normal'
                        else:
                            raise exceptions.ZoneError(
                                f'line {line_num}: hub "{key}": invalid zone "{metadata.get("zone")}", expected one of {standard_zones}'
                            )
                            
                        hub_info['color'] = cls.get_color(line)
                        if hub_info['color'] is None or hub_info['color'] == 'outstandard':
                            hub_info['color'] = '\x1b[0m'
                        
                        try:
                            hub_info['max_drones'] = int(metadata.get('max_drones')) if metadata.get('max_drones') is not None else 1
                            if metadata.get('max_drones') is not None and int(metadata.get('max_drones')) < 0:
                                raise exceptions.NegativeError(
                                    f'line {line_num}: hub "{key}": max_drones must be >= 0, got {metadata.get("max_drones")}'
                                )
                        except ValueError:
                            raise exceptions.NotIntError(
                                f'line {line_num}: hub "{key}": max_drones must be an integer, got "{metadata.get("max_drones")}"'
                            )
                        data.append(hub_info)
                        if cls.doubled_name(data):
                            raise exceptions.DoubledNameError(f'line {line_num}: zone name "{key}" is doubled')
        return data
    
    # Auxiliar method
    @staticmethod
    def connections_repeat(connections: list[dict[str, str]]):
        seen: list[tuple[str, str]] = []
        for connection in connections:
            a: str = connection['connection1'].strip()
            b: str = connection['connection2'].strip()
            pair: tuple[str, str] = tuple(sorted((a, b)))
            if pair in seen:
                return True
            seen.append(pair)
        return False
    
    # Auxiliar method
    @staticmethod
    def new_link(connections: list[dict[str, str]], defined: list[str]) -> bool:
        for connection in connections:
            a = connection['connection1'].strip()
            b = connection['connection2'].strip()
            if a not in defined or b not in defined:
                return True  # unknown zone → error
        return False

    @classmethod
    def defined_zones(cls) -> list[str]:
        names: list[str] = []
        with open('input_file.txt') as input_file:
            for line in input_file:
                if line.startswith('start_hub:') or line.startswith('end_hub:') or line.startswith('hub:'):
                    names.append(line.split()[1])  # the zone name
        return names
    
    @classmethod
    def get_connections(cls) -> list[dict[str, str]]:
        defined = cls.defined_zones()
        connection_info: list[dict] = []

        with open('input_file.txt') as input_file:
            for line_num, line in enumerate(input_file, start=1):
                if line.startswith('connection'):
                    connection = line.split(':')[1].strip()
                    metadata: dict[str, str] = {}

                    if cls.metadata(line):
                        if not cls.bracket_validator(line):
                            raise exceptions.OpenBracketError(f'line {line_num}: Unclosed brackets in metadata: "{line.strip()}"')
                        
                        metadata = cls.parse_metadata(line, line_num)
                        connection = connection.split('[')[0].strip()

                    first, second = connection.split('-')
                    entry = {
                        'connection1': first.strip(),
                        'connection2': second.strip(),
                    }
                    if 'max_link_capacity' in metadata:   
                        try:                         
                            entry['max_link_capacity'] = int(metadata['max_link_capacity'])
                            if int(metadata['max_link_capacity']) < 0:
                                raise exceptions.NegativeError(f'line {line_num}: max_link_capacity ({metadata['max_link_capacity']}) must be a positive integer')
                        except ValueError:
                            raise exceptions.NotIntError(f'line {line_num}: "{metadata['max_link_capacity']}" is not an integer')
                    else:
                        entry['max_link_capacity'] = 1
                    connection_info.append(entry)
                    if cls.connections_repeat(connection_info):
                        raise exceptions.RepeatedConnectionError(f'line {line_num}: {first.strip()}-{second.strip()} is a repeated connection')
                    
                    if cls.new_link(connection_info, defined):
                        raise exceptions.NewLinkWError(f'line {line_num}: non defined name in line "{line.strip()}"')

        return connection_info
