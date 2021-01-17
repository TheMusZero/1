import pygame

from Enemy import Enemy
from Game import Game
from Hero import Hero
from labirint import Labirint, WINDOW_SIZE, ENEMY_EVENT_TYPE, FPS


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    labirint = Labirint("simple_map.txt", [0, 2], 2)
    hero = Hero((7, 7))
    enemy = Enemy((7, 1))
    game = Game(labirint, hero, enemy)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == ENEMY_EVENT_TYPE:
                game.move_enemy()
        game.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
