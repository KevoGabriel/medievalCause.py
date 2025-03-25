#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
          # Aumentando para 2x o tamanho original
        self.surf = pygame.transform.scale_by(self.surf, 2)
        
             # Espelhando horizontalmente (flip no eixo X)
        self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        self.rect.centerx -= 3
        if self.rect.right <= 0:
            self.rect.left = 1920 + 50 # Como meu jogo não terá levels, achei valido deixar dessa forma para que tenha 
                                            # tenha cada vez mais esqueletos para o player desviar/matar.
