#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import W_WIDTH, COLOR_DARKBLUE, BORDER_COLOR, BACKGROUND_COLOR, \
    BORDER_PADDING, CORNER_RADIUS, MENU_OPTION, COLOR_BLUE


# Configuração da Janela
class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/Menubg.png')
        self.rect = self.surf.get_rect(left=0,top=0)

    def run(self, ):
    # Carregamento e reprodução da Música
        pygame.mixer_music.load('./asset/MúsicaTemaJogo.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        menu_option = 0

    # Loop principal do texto do menu
        while True:
            self.window.blit(source=self.surf, dest=self)
            self.menu_text(50, "Mountain",COLOR_DARKBLUE, ((W_WIDTH / 2), 70))
            self.menu_text(50, "Shooter",COLOR_DARKBLUE, ((W_WIDTH / 2), 120))

        # Desenha as opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i],COLOR_BLUE,((W_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i],COLOR_DARKBLUE,((W_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()


# Verificar EVENTOS
    # Quitar do Game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    # ---------------------------------------------

    # Mover para as opções de baixo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
    # ---------------------------------------------

    # Mover para as opções de cima
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
    # ---------------------------------------------

    # Mover para as opções de cima
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]
    # ---------------------------------------------

# Design do texto Mountain Shooter
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Ubuntu Bold", size=text_size)

    # Renderiza o texto para obter seu tamanho
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

    # Define as dimensões do retângulo de fundo e da borda
        background_rect = text_rect.inflate(BORDER_PADDING * 2, BORDER_PADDING * 2)

    # Desenha o retângulo de fundo com cantos arredondados
        pygame.draw.rect(self.window, BACKGROUND_COLOR, background_rect, border_radius=CORNER_RADIUS)
    # Desenha a borda do fundo com cantos arredondados
        pygame.draw.rect(self.window, BORDER_COLOR, background_rect, 1, border_radius=CORNER_RADIUS)

    # Renderiza e desenha o texto principal
        self.window.blit(source=text_surf, dest=text_rect)

