#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import BORDER_PADDING, CORNER_RADIUS, BORDER_COLOR, BACKGROUND_COLOR, COLOR_DARKBLUE, MENU_OPTION, \
    EVENT_ENEMY
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        # Opções do Menu
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    # ------------------------------------------
    # Reproduzir a música
    def run(self):
        pygame.mixer_music.load('./asset/Level1-Welcome To The Jungle.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        clock = pygame.time.Clock()
        # ------------------------------------------

        # Começo do Looping
        while True:
            clock.tick(120)
            # DESENHO DE ENTIDADES
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            # ------------------------------------------
            # MOSTRAR O FPS
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_DARKBLUE, (10, 10))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_DARKBLUE, (55, 10))
            # ATUALIZAR TELA
            pygame.display.flip()
            # VERIFICAR RELACIONAMENTOS DE ENTIDADES
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # ------------------------------------------
            # CONFERIR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
        pass

    # Design do texto Level
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Ubuntu Bold", size=text_size)

        # Renderiza o texto para obter seu tamanho
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])

        # Define as dimensões do retângulo de fundo e da borda
        background_rect = text_rect.inflate(BORDER_PADDING * 1, BORDER_PADDING * 1)

        # Desenha o retângulo de fundo com cantos arredondados
        pygame.draw.rect(self.window, BACKGROUND_COLOR, background_rect, border_radius=CORNER_RADIUS)
        # Desenha a borda do fundo com cantos arredondados
        pygame.draw.rect(self.window, BORDER_COLOR, background_rect, 1, border_radius=CORNER_RADIUS)

        # Renderiza e desenha o texto principal
        self.window.blit(source=text_surf, dest=text_rect)
