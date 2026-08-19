import pygame
import sys
from hub import Hub
from colorama import Fore


class Display():
    
    @staticmethod
    def draw_connection(screen, hub: Hub, second_hub: Hub, connections: list[dict]):
        font = pygame.font.Font(None, 25)
        xline = font.render('-', False, 'White')
        yline = font.render('|', False, 'White')
        con1_x = hub.position[0] * 34 + 25
        con1_y = hub.position[1] * 34 + 4
        con2_x = second_hub.position[0] * 34 + 25
        con2_y = second_hub.position[1] * 34 + 4
           
    
        

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
    def zones(cls, surfaces, all_hubs, screen, text_font, start_subtitle, end_subtitle, symbol, underline, connections: list[dict]):
        for surface, hub in zip(surfaces, all_hubs.values()):
            screen.blit(surface, (hub.position[0] * 34, hub.position[1] * 34))
            hub_subtitle = text_font.render(hub.name, False, 'White')
            
            if hub.role == 'start':
                screen.blit(start_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 12))
            elif hub.role == 'end':
                screen.blit(end_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 12))
            elif hub.role == 'hub':
                screen.blit(hub_subtitle, (hub.position[0] * 34, hub.position[1] * 34 - 12))
            for connection in connections:
                if connection['connection1'] == hub.name:
                    cls.draw_connection(screen, hub, all_hubs[connection['connection2']], connections)

            # if symbol != underline:
            #     screen.blit(symbol, (hub.position[0] * 34 + 9, hub.position[1] * 34 + 6))
            # else:
            #     screen.blit(symbol, (hub.position[0] * 34 + 7, hub.position[1] * 34 - 2))
        
        
    @classmethod
    def display(cls, path, all_hubs: dict[str, Hub], connections: list[dict]):
        pygame.init()
        pygame.display.set_caption('Fly_in')

        surfaces: list = []
        
        screen: pygame = pygame.display.set_mode((1600, 900))
        clock = pygame.time.Clock()

        font = pygame.font.Font(None, 10)
        text_font = pygame.font.Font(None, 20)
        underline = font.render('_', False, 'Black')
        pipe = font.render('|', False, 'Black')
        slash = font.render('/', False, 'Black')
        bslash = font.render('\\', False, 'Black')
        symbols = [underline, bslash, pipe, slash]

        start_name = next((hub.name for hub in all_hubs.values() if hub.role == 'start'), 'start')
        start_subtitle = text_font.render(start_name, False, 'White')
        end_name = next((hub.name for hub in all_hubs.values() if hub.role == 'end'), 'end')
        end_subtitle = text_font.render(end_name, False, 'White')
        
        for hub in all_hubs.values():
            surfaces.append(cls.create_hub())
            
        for surface, hub in zip(surfaces, all_hubs.values()):
            cls.associate_color(hub, surface)

        frame = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            screen.fill((50, 50, 50))

            symbol = symbols[(frame // 20) % 4]

            cls.zones(surfaces, all_hubs, screen, text_font, start_subtitle, end_subtitle, symbol, underline, connections)
            
            frame += 1
            pygame.display.update()
            clock.tick(240)

