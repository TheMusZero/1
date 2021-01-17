import pygame
from game_config import config
from AssetManager import assetManager
from Grass import GrassGroup
from Box import BoxGroup
from Player import PlayerGroup
from Camera import camera


class LevelScreen:
    def __init__(self):
        self.screen = config.get_value('screen')
        level = self.load_level(config.get_value('level'))
        level = [list(line) for line in level]
        self.groups = {'grass': GrassGroup(level), 'box': BoxGroup(level), 'player': PlayerGroup(level)}
        self.groups['player'].set_walls(self.groups['box'])
        camera.update(self.groups['player'].player)

    def draw(self, dt=None):
        self.screen.fill(pygame.Color('black'))
        camera.apply_group(*self.groups.values())
        for group_name in self.groups:
            self.groups[group_name].draw(self.screen)

    def on_event(self, event):
        if event.type == pygame.KEYUP:
            self.groups['player'].on_key_pressed(event.key)

    def load_level(self, level):
        return assetManager.load_level(f'levels/{level}.txt')

    def update(self):
        for group_name in self.groups:
            self.groups[group_name].update()
