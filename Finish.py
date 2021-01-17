from LevelGroup import LevelGroup
from LevelSprite import LevelSprite


class Finish(LevelSprite):

    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'finish.png', groups)


class FinishGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = ['$']
        self.sprite_class = Finish
        self.create_sprites()
