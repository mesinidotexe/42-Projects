import pygame
import sys
from hub import Hub
from colorama import Fore


class Display():

    @staticmethod
    def create_hub():
        return pygame.Surface((25,25))
    
    
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
                screen.blit(start_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 12))
            elif hub.role == 'end':
                screen.blit(end_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 12))
            elif hub.role == 'hub':
                screen.blit(hub_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 12))    
    
    
    @staticmethod
    def draw_line(connections, screen, all_hubs):
        white = (255, 255, 255)
        for hub in all_hubs.values():
            for connection in connections:
                if connection['connection1'] == hub.name:
                    pygame.draw.line(screen, white, (hub.position[0] * 34 + 25, hub.position[1] * 34 + 12), (all_hubs[connection['connection2']].position[0] * 34, all_hubs[connection['connection2']].position[1] * 34 + 12), 1)
    
        
    @staticmethod
    def zones(surfaces, all_hubs: dict[str, Hub], screen):
        for surface, hub in zip(surfaces, all_hubs.values()):
            screen.blit(surface, (hub.position[0] * 34, hub.position[1] * 34))
        
        
    @staticmethod
    def drones(all_hubs, symbol, underline, screen):
        for hub in all_hubs.values():
            if symbol != underline:
                screen.blit(symbol, (hub.position[0] * 34 + 9, hub.position[1] * 34 + 6))
            else:
                screen.blit(symbol, (hub.position[0] * 34 + 7, hub.position[1] * 34 - 2))
        
        
    @classmethod
    def display(cls, path, all_hubs: dict[str, Hub], connections: list[dict]):
        pygame.init()
        pygame.display.set_caption('Fly_in')

        surfaces: list = []
        
        screen: pygame = pygame.display.set_mode((1600, 900))
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
            cls.drones(all_hubs, symbol, underline, screen)
            
        
            frame += 1
            pygame.display.update()
            clock.tick(240)

