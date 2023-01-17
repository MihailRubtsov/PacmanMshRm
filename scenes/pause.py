"""Класс сцены паузы. Открывается при нажатии 'P'"""
import pygame
from constants import WHITE, BLACK
from objects.text import TextObject
from scenes.base import BaseScene
from objects.button import ButtonObject


class PauseScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.objects.append(TextObject(self.game, self.game.width // 2, self.game.height // 2 - 200, 'ПАУЗА', WHITE))
        self.objects.append(ButtonObject(self.game, self.game.width // 2 - 100, self.game.height // 2 - 60, 200, 50,
                                         BLACK, self.resume, text='продолжить'))
        self.objects.append(ButtonObject(self.game, self.game.width // 2 - 100, self.game.height // 2, 200, 50,
                                         BLACK, self.quit, text='выйти в меню'))

    def process_event(self, event):
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            self.game.set_scene(self.game.SCENE_GAME)

    def resume(self):
        self.game.set_scene(self.game.SCENE_GAME)

    def quit(self):
        self.game.scenes[self.game.SCENE_GAME].reset()
        self.game.set_scene(self.game.SCENE_MENU)
