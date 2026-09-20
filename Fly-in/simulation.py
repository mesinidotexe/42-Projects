import pygame
import sys
from hub import Hub
from colorama import Fore


class Display():

    @staticmethod
    def create_hub():
        return pygame.Surface((26,26))
    
    
    @staticmethod
    def associate_color(hub, surface):
        if hub.color == Fore.BLACK:
            surface.fill('Black')
        elif hub.color == Fore.BLUE:
            surface.fill('Blue')
        elif hub.color == Fore.CYAN:
            surface.fill('Cyan')
        elif hub.color == Fore.GREEN:
            surface.fill('Green')
        elif hub.color == Fore.MAGENTA:
            surface.fill('MAGENTA')
        elif hub.color == Fore.RED:
            surface.fill('Red')
        elif hub.color == Fore.WHITE:
            surface.fill('White')
        elif hub.color == Fore.YELLOW:
            surface.fill('Yellow')
        elif hub.color == Fore.LIGHTBLACK_EX or hub.color == '\x1b[0m':
            surface.fill('Gray')
        
    
    @staticmethod
    def zone_name(hubs_width, hubs_height, all_hubs, screen, text_font):

        start_name = next((hub.name for hub in all_hubs.values() if hub.role == 'start'), 'start')
        start_subtitle = text_font.render(start_name, False, 'White')
        end_name = next((hub.name for hub in all_hubs.values() if hub.role == 'end'), 'end')
        end_subtitle = text_font.render(end_name, False, 'White')
        
        for hub in all_hubs.values():
            hub_subtitle = text_font.render(hub.name, False, 'White')

            x = (1600 / hubs_width) * hub.position[0] + 1600 / (hubs_width * 2)
            y = ((900 / hubs_height) * hub.position[1] + 900 / hubs_height) - 15 

            if hub.role == 'start':
                screen.blit(start_subtitle, (x,y))
            elif hub.role == 'end':
                screen.blit(end_subtitle, (x,y))
            elif hub.role == 'hub':
                screen.blit(hub_subtitle, (x,y))    
    
    
    @staticmethod
    def draw_line(hubs_width, hubs_height, connections, screen, all_hubs: dict[str, Hub]):
        white = (255, 255, 255)
        for hub in all_hubs.values():
            for connection in connections:
                if connection['connection1'] == hub.name:
                    x1 = (1600 / hubs_width) * hub.position[0] + 1600 / (hubs_width * 2)
                    y1 = (900 / hubs_height) * hub.position[1] + 900 / hubs_height
                    x2 = (1600 / hubs_width) * all_hubs[connection['connection2']].position[0] + 1600 / (hubs_width * 2)
                    y2 = (900 / hubs_height) * all_hubs[connection['connection2']].position[1] + 900 / hubs_height
                    pygame.draw.line(screen, white, (x1, y1), (x2, y2), 1)
    
        
    @staticmethod
    def zones(hubs_width, hubs_height, surfaces, all_hubs: dict[str, Hub], screen):
        for surface, hub in zip(surfaces, all_hubs.values()):
            x = (1600 / hubs_width) * hub.position[0] + 1600 / (hubs_width * 2)
            y = (900 / hubs_height) * hub.position[1] + 900 / hubs_height
            screen.blit(surface, (x, y))
        
        
    @staticmethod
    def drones(hubs_width, hubs_height, screen, all_hubs: dict[str, Hub], text_font, path: list[dict[str,]], frame, symbol):
        for hub in all_hubs.values():
            test_drone = text_font.render('X', False, 'Black')
            
            n_hops = len(path) - 1

            hop = frame // 200
            t = (frame % 200) / 200
            
            if hop >= n_hops:
                hop = n_hops - 1
                t = 1.0

            start = all_hubs[path[hop]]
            end = all_hubs[path[hop + 1]]
            
            x0 = (1600 / hubs_width) * hub.position[0] + 1600 / (hubs_width * 2)
            y0 = (900 / hubs_height) * hub.position[1] + 900 / hubs_height
            x1 = end.position[0] * 34 + 8
            y1 = end.position[1] * 34 + 7
            
            # (x1 - x0) is the full horizontal distance. Multiply by t and you take that fraction of it.
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            screen.blit(test_drone, (x, y))
        
    

    @staticmethod
    def find_hubs_size(all_hubs: dict[str, Hub]):
        lowx = min(hub.position[0] for hub in all_hubs.values())
        highx = max(hub.position[0] for hub in all_hubs.values())
        
        lowy = min(hub.position[1] for hub in all_hubs.values())
        highy = max(hub.position[1] for hub in all_hubs.values())

        return (highx - lowx + 1, highy - lowy + 1)



    @staticmethod
    def normalize_hubs_position(all_hubs: dict[str, Hub]) -> None:
        lowx = min(hub.position[0] for hub in all_hubs.values())
        lowy = min(hub.position[1] for hub in all_hubs.values())
        
        for hub in all_hubs.values():
            hub.position[0] -= lowx / 2
            hub.position[1] -= lowy / 2
            print(hub.position)



    @classmethod
    def display(cls, path, all_hubs: dict[str, Hub], connections: list[dict]):
        pygame.init()
        pygame.display.set_caption('Fly_in')

        surfaces: list[pygame.Surface] = []
        
        screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
        clock = pygame.time.Clock()

        text_font = pygame.font.Font(None, 20)
        font = pygame.font.Font(None, 20)
        underline = font.render('_', False, 'Black')
        pipe = font.render('|', False, 'Black')
        slash = font.render('/', False, 'Black')
        bslash = font.render('\\', False, 'Black')
        
        for hub in all_hubs.values():
            surfaces.append(cls.create_hub())
            
        for surface, hub in zip(surfaces, all_hubs.values()):
            cls.associate_color(hub, surface)

        symbols = [underline, bslash, pipe, slash]
        hubs_size = cls.find_hubs_size(all_hubs)
        hubs_width = hubs_size[0]
        hubs_height = hubs_size[1]
        
        cls.normalize_hubs_position(all_hubs)

        frame = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            screen.fill((50, 50, 50))

            symbol = symbols[(frame // 20) % 4]

            cls.draw_line(hubs_width, hubs_height, connections, screen, all_hubs)
            cls.zone_name(hubs_width, hubs_height, all_hubs, screen, text_font)
            cls.zones(hubs_width, hubs_height, surfaces, all_hubs, screen)
            cls.drones(hubs_width, hubs_height, screen, all_hubs, text_font, path, frame, symbol)
            
        
            frame += 1
            pygame.display.update()
            clock.tick(240)

