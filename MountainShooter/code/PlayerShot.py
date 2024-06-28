# PlayerShot.py

import pygame
from code.Const import ENTITY_SPEED, PLAYER_KEY_SHOOT
from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.frames_shot = []
        self.frames_explosion = []
        self.load_animation_frames()
        self.current_frame = 0
        self.animation_speed = 5
        self.animation_counter = 0
        self.is_exploding = False

    def load_animation_frames(self):
# Animações dos tiros dos Players
        pressed_key = pygame.key.get_pressed()
# ---------------------------------------
# Tiro Player 1
        if pressed_key[PLAYER_KEY_SHOOT['Player1']]:
            for i in range(1, 4):  # Supondo que você tenha 5 quadros de animação para o tiro
                frame = pygame.image.load(f'./asset/Player1ShotAnimation/{self.name}_anim_{i}.png').convert_alpha()
                self.frames_shot.append(frame)

# Explosão Player 1
            for i in range(5, 8):  # Supondo que você tenha 5 quadros de animação para a explosão
                frame = pygame.image.load(f'./asset/Player1ShotAnimation/{self.name}_anim_{i}.png').convert_alpha()
                self.frames_explosion.append(frame)
# ---------------------------------------
# Tiro Player 2
        if pressed_key[PLAYER_KEY_SHOOT['Player2']]:
            for i in range(1, 4):  # Supondo que você tenha 5 quadros de animação para o tiro
                frame = pygame.image.load(f'./asset/Player2ShotAnimation/{self.name}_anim_{i}.png').convert_alpha()
                self.frames_shot.append(frame)
# Explosão Player 2
        # Carregue as imagens da animação da explosão
            for i in range(5, 8):  # Supondo que você tenha 5 quadros de animação para a explosão
                frame = pygame.image.load(f'./asset/Player2ShotAnimation/{self.name}_anim_{i}.png').convert_alpha()
                self.frames_explosion.append(frame)

# ---------------------------------------
    def move(self):
        if not self.is_exploding:
            self.rect.centerx += ENTITY_SPEED[self.name]
        self.animate()

    def animate(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            if not self.is_exploding:
                self.current_frame = (self.current_frame + 1) % len(self.frames_shot)
                self.surf = self.frames_shot[self.current_frame]
            else:
                if self.current_frame < len(self.frames_explosion) - 1:
                    self.current_frame += 1
                    self.surf = self.frames_explosion[self.current_frame]
                else:
                    self.health = 0  # Destrói o tiro após a animação de explosão

    def start_explosion(self):
        self.is_exploding = True
        self.current_frame = 0
        self.animation_counter = 0
