#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Level import Level
from code.Menu import Menu
from code.const import MENU_OPT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (1920, 1080))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return == MENU_OPT[0]:
                level = Level(self.window, "Level1", menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPT[2]:
                pygame.quit()
                quit()
            else:
                pass
                
        
          