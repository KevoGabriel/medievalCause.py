#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background

class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
            match entity_name:
                case "Menu_battle":
                    list_bg = []
                    for i in range(1):
                        list_bg.append(Background(f"Menu_battle{i}", (0, 0)))
                    return list_bg