#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
            match entity_name:
                case "Menu_battle":
                    list_bg = []
                    for i in range(1):
                        list_bg.append(Background(f"Menu_battle{i}", (0, 0)))
                    return list_bg
                case "Player1":
                    return Player("Player1", (int(1920/2), int(1080/2)))
                case "Enemy1":
                    return Enemy("Enemy1", ((1920), random.randint(450, 1000)))