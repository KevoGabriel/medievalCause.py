import pygame

pygame.init()
window = pygame.display.set_mode(size = (600, 480))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Evento contido nos contents
            pygame.quit() # Close Window
            quit() # end pygame
            