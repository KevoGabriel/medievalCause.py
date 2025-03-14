#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import MENU_OPT

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menu_battle.png")
        self.rect = self.surf.get_rect(left=0, top=0)
            
    

    def run(self, ):
        pygame.mixer_music.load("./asset/MedievalCause.mp3")
        pygame.mixer_music.play(-1)
        while True:
            
            self.window.blit(source=self.surf, dest=self.rect)
            
            self.menu_text(170, "Medieval", (227, 4, 0), ((1920 / 2), 120))
            self.menu_text(170, "Cause", (227, 4, 0), ((1920 / 2), 280))
            
            for i in range(len(MENU_OPT)):
                self.menu_text(90, MENU_OPT[i], (255, 255, 255), ((1920 / 2), 600 + 90 * i))

            pygame.display.flip()
            
              #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Evento contido nos contents
                    pygame.quit() # Close Window
                    quit() # end pygame
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Times New Roman", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)