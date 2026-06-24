#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        # move up
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 3:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # move down
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT - 3:
            self.rect.centery += ENTITY_SPEED[self.name]

        # move left
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 3:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # move right
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH - 3:
            self.rect.centerx += ENTITY_SPEED[self.name]

        # shoot

    def shoot(self):
        self.shoot_delay -=1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShoot(name=f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery))

