import pygame

from Finish import FinishGroup
from Floor import FloorGroup
from Lava import LavaGroup
from game_config import config
from AssetManager import assetManager
from Box import BoxGroup
from Player import PlayerGroup
from Camera import camera
from Enemy import EnemyGroup


class LevelScreen:
    def __init__(self):
        self.screen = config.get_value('screen')
        self.levels = ['lvl1', 'lvl2', 'lvl4', 'lvl5', 'lvl6']
        config.set_value('level', self.levels[0])
        self.init_level()

    def init_level(self):
        self.screen = config.get_value('screen')
        level = self.load_level(config.get_value('level'))
        level = [list(line) for line in level]
        player_group = PlayerGroup(level)
        self.groups = {'floor': FloorGroup(level), 'box': BoxGroup(level), 'player': player_group,
                       'lava': LavaGroup(level), 'enemy': EnemyGroup(level, player_group.player),
                       'finish': FinishGroup(level)}
        self.groups['player'].set_walls(self.groups['box'])
        self.groups['player'].set_finish(self.groups['finish'])
        camera.update(self.groups['player'].player)

    def next_level(self):
        level = config.get_value('level')
        new_level_index = self.levels.index(level) + 1
        if new_level_index >= len(self.levels):
            # все уровни пройдены, в этом случае надо что-то сделать, сейчас просто зациклил уровни
            new_level_index = 0
        config.set_value('level', self.levels[new_level_index])
        self.init_level()

    def draw(self, dt=None):
        self.screen.fill(pygame.Color('black'))
        camera.apply_group(*self.groups.values())
        for group_name in self.groups:
            self.groups[group_name].draw(self.screen)

    def on_event(self, event):
        if event.type == pygame.KEYUP:
            self.groups['player'].on_key_pressed(event.key)
        if event.type == config.get_value('level_end_event'):
            self.next_level()

    def load_level(self, level):
        return assetManager.load_level(f'levels/{level}.txt')

    def update(self):
        for group_name in self.groups:
            self.groups[group_name].update()
