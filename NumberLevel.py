import pygame


def draw_number_level(screen, level):
    font = pygame.font.Font(None, 32)
    text = font.render(level, True, [255, 255, 255])
    screen.blit(text, (0, 0))
