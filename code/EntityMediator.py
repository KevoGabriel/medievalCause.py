import pygame
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:  
    
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
    
    @staticmethod
    def __verify_collision_entity(ent1, ent2):   
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            player = ent1
            enemy = ent2
        elif isinstance(ent2, Player) and isinstance(ent1, Enemy):
            player = ent2
            enemy = ent1
        else:
            return  # Ignora se não for uma colisão entre player e inimigo

        # Se o jogador está atacando, verifica colisão com hitbox do ataque
        if player.is_attacking:
            attack_rect = player.get_attack_rect()
            if attack_rect and attack_rect.colliderect(enemy.rect):
                enemy.health = 0  # Inimigo morre
                enemy.last_dmg = player.name
                return  # Evita aplicar dano ao jogador nesta situação

        if player.rect.colliderect(enemy.rect) and not player.invulnerable:
            player.health -= enemy.damage
            player.last_dmg = enemy.name
            enemy.last_dmg = player.name
            player.invulnerable = True
            player.invuln_timer = pygame.time.get_ticks()
            
            hit_sound = pygame.mixer.Sound("./asset/PlayerDamage.mp3")  # Carrega o som de hit
            hit_sound.play()


    
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)
                
               
                       
    @staticmethod        
    def verify_health(entity_list: list[Entity]) -> int:
        killed = 0
        for ent in entity_list[:]:  # copia da lista para não dar erro ao remover
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    killed += 1
                    enemy_death_sound = pygame.mixer.Sound("./asset/EnemyDeath.mp3")
                    enemy_death_sound.play()
                entity_list.remove(ent)
        return killed
