#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.original_surf = pygame.transform.scale_by(self.surf, 2)
        self.surf = self.original_surf
        self.attack_surf = pygame.transform.scale_by(
            pygame.image.load(f"./asset/Player_attack.png").convert_alpha(), 2
        )

        # Carrega o som de ataque
        self.attack_sound = pygame.mixer.Sound("./asset/Hit.mp3")

        self.facing_left = False
        self.is_attacking = False
        self.attack_timer = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP] and self.rect.top > 450:
            self.rect.centery -= 8
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < 1000:
            self.rect.centery += 8
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 6
            if not self.facing_left:
                self._flip_images()
                self.facing_left = True
        if pressed_key[pygame.K_RIGHT] and self.rect.right < 1920:
            self.rect.centerx += 6
            if self.facing_left:
                self._flip_images()
                self.facing_left = False

        if pressed_key[pygame.K_RCTRL] and not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = pygame.time.get_ticks()
            self.surf = self.attack_surf
            self.attack_sound.play()  # 🔊 TOCA O SOM DE ATAQUE

        if self.is_attacking and pygame.time.get_ticks() - self.attack_timer > 200:
            self.surf = self.original_surf
            self.is_attacking = False

    def _flip_images(self):
        self.surf = pygame.transform.flip(self.surf, True, False)
        self.attack_surf = pygame.transform.flip(self.attack_surf, True, False)
        self.original_surf = pygame.transform.flip(self.original_surf, True, False)
