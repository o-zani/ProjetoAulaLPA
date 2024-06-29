#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import BORDER_PADDING, BORDER_COLOR, BACKGROUND_COLOR, COLOR_DARKBLUE, MENU_OPTION, \
    EVENT_ENEMY, CORNER_RADIUS_INFO_SCREEN, EVENT_TIMEOUT, EVENT_START_GAME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, menu_option: str, player_score: list[int]):
        self.window: Surface = window
        self.name = name
        # Opções do Menu
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, 2000)  # 4 segundos por entidade
        self.timeout = 30000  # 30 segundos por fase
        pygame.time.set_timer(EVENT_TIMEOUT, 100)  # 100ms  # 4 segundos por entidade

    # ------------------------------------------

    # Reproduzir a música
    def run(self, player_score: list[int]):
        # Carregar e tocar a música do nível
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
                #  Mostrar Vida e Score dos Players
                if ent.name == 'Player1':
                    self.level_text(14, f'P1 Vida: {ent.health} | Score: {ent.score}', COLOR_DARKBLUE, (10, 10))
                if ent.name == 'Player2':
                    self.level_text(14, f'P2 Vida: {ent.health} | Score: {ent.score}', COLOR_DARKBLUE, (10, 25))
            # ------------------------------------------
            # Mostrar O FPS
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_DARKBLUE, (465, 10))
            # Mostrar o Level
            self.level_text(30, f'{self.name} ', COLOR_DARKBLUE, (270, 5))
            # Mostrar o Timer
            self.level_text(25, f'Tempo Restante - {self.timeout / 1000}s', COLOR_DARKBLUE, (215, 32))
            # Mostrar Entidades
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_DARKBLUE, (510, 10))
            # Atualizar Tela
            pygame.display.flip()
            # Verificar Relacionamentos de entidades
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

                if event.type == EVENT_TIMEOUT:  #acontece a cada 100ms
                    self.timeout -= 100  # timeout começa com 20000
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

    # Design do texto Level
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Ubuntu Bold", size=text_size)

        # Renderiza o texto para obter seu tamanho
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])

        # Define as dimensões do retângulo de fundo e da borda
        background_rect = text_rect.inflate(BORDER_PADDING * 1, BORDER_PADDING * 1)

        # Desenha o retângulo de fundo com cantos arredondados
        pygame.draw.rect(self.window, BACKGROUND_COLOR, background_rect, border_radius=CORNER_RADIUS_INFO_SCREEN)
        # Desenha a borda do fundo com cantos arredondados
        pygame.draw.rect(self.window, BORDER_COLOR, background_rect, 1, border_radius=CORNER_RADIUS_INFO_SCREEN)

        # Renderiza e desenha o texto principal
        self.window.blit(source=text_surf, dest=text_rect)
