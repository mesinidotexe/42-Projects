import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))  # window size
clock = pygame.time.Clock()

running = True
while running:
    # 1. Handle events (input, closing window, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game state (move things, check collisions, etc.)
    # ... your logic goes here

    # 3. Draw everything
    screen.fill((30, 30, 30))  # clear screen with a dark gray
    # ... draw shapes/images here

    pygame.display.flip()  # show what we just drew
    clock.tick(60)  # limit to 60 frames per second

pygame.quit()