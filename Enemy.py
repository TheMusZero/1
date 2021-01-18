import pygame
from copy import deepcopy

from LevelGroup import LevelGroup
from LevelSprite import LevelSprite
from game_config import config
from WaveSearchPath import WaveSearchPath


class Enemy(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'enemy.png', groups)
        self.search = WaveSearchPath()
        self.walls = ['~', '#']
        self.player = None

        self.counter = 0

    def get_coords(self):
        tile_size = config.get_value('tile_size')
        x = self.col * tile_size + tile_size // 2 - self.rect.width // 2
        y = self.row * tile_size + tile_size // 2 - self.rect.height // 2
        return x, y

    def set_player(self, player):
        self.player = player

    # преобразуем нашу карту уровня в карту, понятную алгоритму поиска
    # все препятствия заменяются на -1, все остальное заменяется на 0
    def level_to_search(self):
        level = deepcopy(self.level)
        width = len(level[0])
        height = len(level)
        for i in range(height):
            for j in range(width):
                val = level[i][j]
                if val in self.walls:
                    level[i][j] = -1
                else:
                    level[i][j] = 0
        return level

    def set_level(self, level):
        self.level = level

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def move(self):
        level = self.level_to_search()
        path = self.search.search((self.row, self.col), (self.player.row, self.player.col), level)
        self.row, self.col = path[1]

    def update(self):
        super().update()

        self.counter += 1
        # у нас 60 кадров - значит враг будет перемещаться каждые 30 кадров - один раз в пол секунды.
        if self.counter % 60  == 0:
            self.move()


class EnemyGroup(LevelGroup):
    def __init__(self, level, player):
        super().__init__(level)
        self.key = '2'
        self.sprite_class = Enemy
        self.create_sprites()
        self.enemy = self.sprites()[0]
        self.enemy.set_player(player)
        self.enemy.set_level(level)
        self.enemy.set_size(self.width, self.height)
