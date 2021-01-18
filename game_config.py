from Config import Config
import pygame

config = Config()
config.set_values(
    {'width': 550, 'height': 550, 'level': 'level1', 'tile_size': 50, 'level_end_event': pygame.USEREVENT + 1})
