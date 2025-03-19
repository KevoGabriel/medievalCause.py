#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
          # Aumentando para 2x o tamanho original
        self.surf = pygame.transform.scale_by(self.surf, 2)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 450: # Assumindo que a area de grama va ate 450px
            self.rect.centery -= 8
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < 1000: # Para o boneco não ficar com a parte do corpo fora da base da tela
            self.rect.centery += 8
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 6
        if pressed_key[pygame.K_RIGHT] and self.rect.right < 1920: 
            self.rect.centerx += 6
        pass
