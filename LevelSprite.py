import pygame
from game_config import config
from AssetManager import assetManager


class LevelSprite(pygame.sprite.Sprite):
    def __init__(self, row, col, image, *groups):
        super().__init__(groups)
        self.image = assetManager.load_image(image)
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.rect.x, self.rect.y = self.get_coords()

    def get_coords(self):
        tile_size = config.get_value('tile_size')
        return self.col * tile_size, self.row * tile_size

    def update(self):
        self.rect.x, self.rect.y = self.get_coords()
