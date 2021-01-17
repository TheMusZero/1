from LevelGroup import LevelGroup
from LevelSprite import LevelSprite


class Box(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'box.png', groups)


class BoxGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = '#'
        self.sprite_class = Box
        self.create_sprites()
