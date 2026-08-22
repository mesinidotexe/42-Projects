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
    def zone_name(all_hubs, screen, text_font):

        start_name = next((hub.name for hub in all_hubs.values() if hub.role == 'start'), 'start')
        start_subtitle = text_font.render(start_name, False, 'White')
        end_name = next((hub.name for hub in all_hubs.values() if hub.role == 'end'), 'end')
        end_subtitle = text_font.render(end_name, False, 'White')
        
        for hub in all_hubs.values():
            hub_subtitle = text_font.render(hub.name, False, 'White')
            
            if hub.role == 'start':
                screen.blit(start_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 13))
            elif hub.role == 'end':
                screen.blit(end_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 13))
            elif hub.role == 'hub':
                screen.blit(hub_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 13))    
    
    
    @staticmethod
    def draw_line(connections, screen, all_hubs):
        white = (255, 255, 255)
        for hub in all_hubs.values():
            for connection in connections:
                if connection['connection1'] == hub.name:
                    pygame.draw.line(screen, white, (hub.position[0] * 34 + 26, hub.position[1] * 34 + 13), (all_hubs[connection['connection2']].position[0] * 34, all_hubs[connection['connection2']].position[1] * 34 + 13), 1)
    
        
    @staticmethod
    def zones(surfaces, all_hubs: dict[str, Hub], screen):
        for surface, hub in zip(surfaces, all_hubs.values()):
            screen.blit(surface, (hub.position[0] * 34, hub.position[1] * 34))
        
        
    @staticmethod
    def drones(screen, all_hubs: dict[str, Hub], text_font, path: list[dict[str,]], frame, symbol):
        test_drone = text_font.render('X', False, 'Black')
        
        n_hops = len(path) - 1

        hop = frame // 200
        t = (frame % 200) / 200
        
        if hop >= n_hops:
            hop = n_hops - 1
            t = 1.0

        start = all_hubs[path[hop]]
        end = all_hubs[path[hop + 1]]
        
        x0 = start.position[0] * 34 + 26
        y0 = start.position[1] * 34 + 7
        x1 = end.position[0] * 34 + 8
        y1 = end.position[1] * 34 + 7
        
        # (x1 - x0) is the full horizontal distance. Multiply by t and you take that fraction of it.
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        screen.blit(test_drone, (x, y))
        
        

    @classmethod
    def display(cls, path, all_hubs: dict[str, Hub], connections: list[dict]):
        pygame.init()
        pygame.display.set_caption('Fly_in')

        surfaces: list[pygame.Surface] = []
        
        screen: pygame.display.set_mode = pygame.display.set_mode((1600, 900))
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
        
        frame = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            screen.fill((50, 50, 50))

            symbol = symbols[(frame // 20) % 4]

            cls.draw_line(connections, screen, all_hubs)
            cls.zone_name(all_hubs, screen, text_font)
            cls.zones(surfaces, all_hubs, screen)
            cls.drones(screen, all_hubs, text_font, path, frame, symbol)
            
        
            frame += 1
            pygame.display.update()
            clock.tick(240)

