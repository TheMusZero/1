from LevelGroup import LevelGroup
from LevelSprite import LevelSprite


class Lava(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'lava.png', groups)


class LavaGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = '~'
        self.sprite_class = Lava
        self.create_sprites()
