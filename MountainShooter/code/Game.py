#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import W_WIDTH, W_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
    # Configurações do MENU

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                level = Level(self.window,'Level1', menu_return)
                level_return = level.run()
                if level_return:
                    Level = Level(self.window,'Level2', menu_return)
                    level_return = level.run()
            else:
                pygame.quit()
                sys.exit()
