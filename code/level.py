#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
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
        self.enemy_spawn_interval = 2000  # Começa com 2 segundos
        self.enemies_killed = 0
        
        self.font = pygame.font.SysFont("Times New Roman", 36)


        

    def run(self):
        pygame.mixer_music.load(f"./asset/FeudalCause.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            
            for ent in self.entity_list:
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)
                
            # Desenhar vida do player no canto superior direito
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    health_text = self.font.render(f"Health: {ent.health}", True, (255, 255, 255))  # Vermelho
                    text_rect = health_text.get_rect(topright=(1900, 10))  # Posição (x, y)
                    self.window.blit(health_text, text_rect)
                    break  # só tem um player

                
            pygame.display.flip()
            
            # Verificação de dano e vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            killed = EntityMediator.verify_health(entity_list=self.entity_list)
            if killed > 0:
                self.enemies_killed += killed
                if self.enemies_killed % 5 == 0 and self.enemy_spawn_interval > 500:
                    self.enemy_spawn_interval -= 200  # Fica mais rápido a cada 5 kills

            
        #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Evento contido nos contents
                    pygame.quit() # Close Window
                    quit() # end pygame
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity("Enemy1"))
                    pygame.time.set_timer(EVENT_ENEMY, self.enemy_spawn_interval)

