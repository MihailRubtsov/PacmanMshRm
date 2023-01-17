"""Класс сцены с настройками"""
from objects.Settings.ButtonsCollection import ButtonsColection
from scenes.base import BaseScene
from objects.text import TextObject
from constants import FONT
import pygame as pg


class SettingsScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.screen = game.screen
        self.buttons = ButtonsColection(game)
        text1 = TextObject(game, self.game.width - 240, self.game.height * 0.67, 'Спец. возможности', (155, 155, 155),
                           FONT, 23)
        text2 = TextObject(game, self.game.width - 240, self.game.height * 0.8, 'Клавиша "z"', (88, 88, 88),
                           FONT, 16)
        text3 = TextObject(game, self.game.width - 240, self.game.height * 0.9, 'Клавиша "x"', (88, 88, 88),
                           FONT, 16)
        self.objects.append(text1)
        self.objects.append(text2)
        self.objects.append(text3)

    def process_logic(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.game_over = True

    def process_event(self, event):
        super().process_event(event)
        if event.type != pg.KEYDOWN:
            return
        if event.key == pg.K_ESCAPE:
            self.buttons.function_back()
            self.game.sounds.mus_switch()

    def process_draw(self):
        self.buttons.prev_settings()
        super().process_draw()
        for btn in self.buttons.buttons:
            btn.draw(self.screen)
