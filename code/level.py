#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.const import EVENT_ENEMY

class Level:
    def __init__(self, window, name, game_mode): #Vou deixar o game_mode, pois no futuro, isoladamente, farei para dois players
        self.window = window
        self.name = name
        self.game_mode = game_mode # E também para não me perder nas aulas práticas xD
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Menu_battle"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))
        self.timeout = 20000
        # Geração do inimigo (evento)
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        pygame.mixer_music.load(f"./asset/FeudalCause.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            
            for ent in self.entity_list:
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)
                
            pygame.display.flip()
            
        #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Evento contido nos contents
                    pygame.quit() # Close Window
                    quit() # end pygame
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity("Enemy1"))
                    
                
