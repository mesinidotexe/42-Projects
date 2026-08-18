import pygame
import sys
from hub import Hub
from colorama import Fore


class Display():
    
    @staticmethod
    def create_hub():
        return pygame.Surface((25,25))
        
    @classmethod
    def display(cls, path, all_hubs: dict[str, Hub]):
        pygame.init()
        pygame.display.set_caption('Fly_in')

        surfaces: list = []
        screen = pygame.display.set_mode((1600, 900))
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 25)
        minus = font.render('-', False, 'Black')
        pipe = font.render('|', False, 'Black')
        slash = font.render('/', False, 'Black')
        bslash = font.render('\\', False, 'Black')
        # Ordered so the symbol appears to rotate: - \ | /
        symbols = [minus, bslash, pipe, slash]
        

        for hub in all_hubs.values():
            surfaces.append(cls.create_hub())
            
        for surface, hub in zip(surfaces, all_hubs.values()):
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
                screen.blit(symbol, (hub.position[0] * 35 + 9, hub.position[1] * 35 + 6))

            frame += 1
                
                
            

            pygame.display.update()
            clock.tick(240)  # limit to 60 frames per second

