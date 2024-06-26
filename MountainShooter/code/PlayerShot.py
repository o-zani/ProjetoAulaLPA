from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    def move(self):
        pass

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]

        pass