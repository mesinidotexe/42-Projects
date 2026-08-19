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
        
    @classmethod
    def display(cls, path, all_hubs: dict[str, Hub]):
        pygame.init()
        pygame.display.set_caption('Fly_in')

        surfaces: list = []
        
        screen = pygame.display.set_mode((1600, 900))
        clock = pygame.time.Clock()

        font = pygame.font.Font(None, 25)
        text_font = pygame.font.Font(None, 20)
        underline = font.render('_', False, 'Black')
        pipe = font.render('|', False, 'Black')
        slash = font.render('/', False, 'Black')
        bslash = font.render('\\', False, 'Black')
        symbols = [underline, bslash, pipe, slash]

        start_subtitle = text_font.render('Start', False, 'White')
        end_subtitle = text_font.render('End', False, 'White')
        
        

        for hub in all_hubs.values():
            surfaces.append(cls.create_hub())
            
        for surface, hub in zip(surfaces, all_hubs.values()):
            cls.associate_color(hub, surface)

        frame = 0
        while True:
            # 1. Handle events (input, closing window, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            symbol = symbols[(frame // 20) % 4]

            for surface, hub in zip(surfaces, all_hubs.values()):
                screen.blit(surface, (hub.position[0] * 35, hub.position[1] * 35))
                hub_subtitle = text_font.render(hub.name, False, 'White')
                
                if hub.role == 'start':
                    screen.blit(start_subtitle, (hub.position[0] * 35, hub.position[1] * 35 - 12))
                elif hub.role == 'end':
                    screen.blit(end_subtitle, (hub.position[0] * 35, hub.position[1] * 35 - 12))
                elif hub.role == 'hub':
                    screen.blit(hub_subtitle, (hub.position[0] * 35, hub.position[1] * 35 - 12))
                    
                if symbol != underline:
                    screen.blit(symbol, (hub.position[0] * 35 + 9, hub.position[1] * 35 + 6))
                else:
                    screen.blit(symbol, (hub.position[0] * 35 + 7, hub.position[1] * 35 - 2))

            frame += 1
                
                
            

            pygame.display.update()
            clock.tick(240)  # limit to 240 frames per second

