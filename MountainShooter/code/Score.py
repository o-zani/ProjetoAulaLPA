import pygame
from pygame import Surface


class Score:

    def __init__(self, window: Surface):
        pass
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self):
        pass

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass
