from game_config import config


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def apply_group(self, *groups):
        for group in groups:
            for sprite in group:
                self.apply(sprite)

    # позиционировать камеру на объекте target
    def update(self, target):
        width, height = config.get_list_values('width', 'height')
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


camera = Camera()
