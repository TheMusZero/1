import pygame

from game_config import config
from GameMain import GameMain


def draw_number_level(screen, level):
    font = pygame.font.Font(None, 32)
    text = font.render(level, True, [0, 0, 0])
    screen.blit(text, (0, 0))


if __name__ == '__main__':
    level = input('Введите название уровня')

    pygame.init()
    pygame.display.set_caption('')
    width, height = config.get_list_values('width', 'height')
    size = width, height
    screen = pygame.display.set_mode(size)
    config.set_value('screen', screen)
    config.set_value('level', level)
    clock = pygame.time.Clock()
    running = True
    game = GameMain()
    fps = 60
    dt = 0
    while running:
        for event in pygame.event.get():
            game.on_event(event)
            draw_number_level(screen, level)
            if event.type == pygame.QUIT:
                running = False
        game.draw(dt)
        game.update()
        pygame.display.flip()
        dt = clock.tick(fps)
    pygame.quit()
