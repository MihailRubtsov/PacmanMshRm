"""Сцена, открывающаяся при первом запуске игры. Наследуется от класса настроек"""
import os.path
import pygame
from scenes.settings import SettingsScene
from constants import SETTINGS_PATH, FONT
from objects.text import TextObject


class FirstTimeSettingsScene(SettingsScene):
    def __init__(self, game):
        super().__init__(game)
        self.objects.append(TextObject(game, game.size[0] // 2, 20, 'Вы впервые запускаете игру', pygame.Color('white'), FONT))
        self.objects.append(TextObject(game, game.size[0] // 2, 50, 'Настройте управление под себя', pygame.Color('white'), FONT))
        self.buttons.buttons[-1].text = 'Принять'  # изменение кнопки выхода
        self.buttons.buttons[-1].padding = 150

    def process_logic(self):
        if os.path.exists(SETTINGS_PATH):
            self.game.set_scene(self.game.SCENE_MENU)
