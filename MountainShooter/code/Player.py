#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect

from code.Const import ENTITY_SPEED, W_HEIGHT, W_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

# ---------------------------------------------
# WASD para mover a nave do Player 1
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: # W
            self.rect.centery -= ENTITY_SPEED[self.name]
            pass

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < W_HEIGHT:# S
            self.rect.centery += ENTITY_SPEED[self.name]
            pass

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: # A
            self.rect.centerx -= ENTITY_SPEED[self.name]
            pass

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < W_WIDTH : # D
            self.rect.centerx += ENTITY_SPEED[self.name]
            pass

