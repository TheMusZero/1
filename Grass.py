from LevelGroup import LevelGroup
from LevelSprite import LevelSprite


class Grass(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'floor.png', groups)


class GrassGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = ['.', '@']
        self.sprite_class = Grass
        self.create_sprites()
