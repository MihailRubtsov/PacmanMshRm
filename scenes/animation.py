"""Анимации на главном меню"""
from objects.animation.pacman_anim import AnimPacman
from objects.animation.ghosts_anim import AnimGhost
from scenes.base import BaseScene
from objects.seed import BigSeed


class AnimationScene(BaseScene):
    start = False
    fear = False

    def __init__(self, game, surface):
        super().__init__(game)
        self.x, self.y = 500, 195  # позиция seed и Y всей анимации
        self.surface = surface

    def all_objects_append(self):
        self.objects.append(BigSeed(self.game, self.x, self.y - 10))
        self.objects.append(
            AnimPacman(self.game, self, self.x, self.x - 100, self.y)
        )
        self.objects.append(AnimGhost(self.game, self, 'images/ghosts/blinky/blinky.png', self.x - 155, self.y - 10))
        self.objects.append(AnimGhost(self.game, self, 'images/ghosts/clyde/clyde.png', self.x - 175, self.y - 10))
        self.objects.append(AnimGhost(self.game, self, 'images/ghosts/inky/inky.png', self.x - 195, self.y - 10))
        self.objects.append(AnimGhost(self.game, self, 'images/ghosts/pinky/pinky.png', self.x - 215, self.y - 10))

    def on_activate(self):
        self.all_objects_append()

    def on_deactivate(self):
        self.objects.clear()
        self.fear = False
        self.start = False
