#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import W_WIDTH, W_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
    def __init__(self):
        while True:
            menu = Menu(self.window)
            menu.run()


