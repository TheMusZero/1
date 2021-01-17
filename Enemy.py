import pygame
from LevelGroup import LevelGroup
from LevelSprite import LevelSprite
from game_config import config
from Camera import camera


class Enemy(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'player.png', groups)
        self.walls = None


    def get_coords(self):
        tile_size = config.get_value('tile_size')
        x = self.col * tile_size + tile_size // 2 - self.rect.width // 2
        y = self.row * tile_size + tile_size // 2 - self.rect.height // 2
        return x, y

    def set_walls(self, walls):
        self.walls = walls

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def move_up(self):
        self.row -= 1

    def move_down(self):
        self.row += 1

    def move_left(self):
        self.col -= 1

    def move_right(self):
        self.col += 1

    def move_action(self, direction, reverse=False):
        if direction in self.actions:
            if reverse:
                self.reverse_actions[direction]()
            else:
                self.actions[direction]()
            self.update()

    def move(self, direction):
        if self.can_move(direction):
            self.move_action(direction)
            camera.update(self)

    def can_move(self, direction):
        result = True
        self.move_action(direction)
        if not (0 <= self.row < self.height and 0 <= self.col < self.width):
            result = False
        if self.walls and pygame.sprite.spritecollideany(self, self.walls):
            result = False
        self.move_action(direction, reverse=True)
        return result


class EnemyGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = '2'
        self.sprite_class = Enemy
        self.create_sprites()
        self.player = self.sprites()[0]
        self.player.set_size(self.width, self.height)

    def set_walls(self, walls):
        self.player.set_walls(walls)

    def on_key_pressed(self, key):
        self.player.move(key)

