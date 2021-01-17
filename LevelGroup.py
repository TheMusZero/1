import pygame


class LevelGroup(pygame.sprite.Group):
    def create_sprites(self):
        width, height = len(self.level), len(self.level[0])
        self.width = width
        self.height = height
        if isinstance(self.key, list):
            keys = self.key
        else:
            keys = [self.key]
        for i in range(height):
            for j in range(width):
                val = self.level[i][j]
                if val in keys:
                    self.sprite_class(i, j, self)

    def __init__(self, level):
        self.level = level
        # Переопределим эти параметры в классах потомках
        self.key = None
        self.sprite_class = None
        super().__init__()
