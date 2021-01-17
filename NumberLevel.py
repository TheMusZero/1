import pygame


class NumberLevel:
    def draw_number_level(self, screen, level):
        font = pygame.font.Font(None, 32)
        text = font.render(level, True, [0, 0, 0])
        screen.blit(text, (0, 0))
