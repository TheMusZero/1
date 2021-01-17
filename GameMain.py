from StartScreen import StartScreen
from LevelScreen import LevelScreen

START_SCREEN = 0
MAIN_SCREEN = 1


class GameMain:
    def __init__(self):
        self.state = START_SCREEN
        self.scenes = [StartScreen(self.next_scene), LevelScreen()]

    def draw(self, dt=None):
        self.get_active_scene().draw(dt)

    def get_active_scene(self):
        return self.scenes[self.state]

    def next_scene(self):
        self.state += 1

    def on_event(self, event):
        self.get_active_scene().on_event(event)

    def update(self):
        self.get_active_scene().update()
