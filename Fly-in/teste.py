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
        surfaces: list = []
        pygame.init()
        pygame.display.set_caption('Fly_in')

        screen = pygame.display.set_mode((800, 400))
        clock = pygame.time.Clock()
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
            elif hub.color == Fore.LIGHTBLACK_EX:
                surface.fill('Gray')

        while True:
            # 1. Handle events (input, closing window, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            for surface, hub in zip(surfaces, all_hubs.values()):
                screen.blit(surface, (hub.position[0] * 25, hub.position[1] * 25))
            

            pygame.display.update()
            clock.tick(60)  # limit to 60 frames per second

