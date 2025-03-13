#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        pygame.init()
        window = pygame.display.set_mode(size = (600, 480))

        while True:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Evento contido nos contents
                    print("quiting...")
                    pygame.quit() # Close Window
                    quit() # end pygame
                    