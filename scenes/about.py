"""Класс сцены, на которой отображены участники проекта"""
from datetime import datetime
import pygame
from constants import WHITE, FONT, ORANGE
from objects.Settings.back_button import BackButton
from objects.text import TextObject
from scenes.base import BaseScene


# Этот класс - поле, которое двигается (так как участников слишком много, и они не помещаются на сцену)
class ScrollSurface:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.surface.Surface((self.game.width, self.game.height * 2))
        self.scroll = 600
        self.last_time = datetime.now()

    def scrolling(self):
        now_time = datetime.now()
        self.scroll -= (now_time - self.last_time).microseconds // 10000
        self.last_time = datetime.now()
        if self.scroll < -self.game.height - 400:
            self.scroll = 600


class AboutScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.surface = ScrollSurface(self.game)
        self.title_font = pygame.font.Font(FONT, 25)
        self.objects.append(TextObject(self.game, 200, self.game.height // 10,
                                       'Над игрой работали:', WHITE, FONT, size=28))
        self.back_button = BackButton(5, 20, self.game, self.function_back, text='Назад')
        self.back_button.padding = 120
        self.developers = [
            'Рубцов Михаил', 'Медведев Роман'
        ]
        self.draw_devs()

    def function_back(self):
        self.game.set_scene(self.game.SCENE_MENU)

    def draw_devs(self):
        x = 585
        y = 110
        for dev in self.developers:
            text = TextObject(self.surface, x, y, dev, ORANGE, FONT)
            self.objects.append(text)
            y += 44

    def process_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            self.function_back()

    def on_activate(self):
        self.surface.scroll = 600

    def process_logic(self):
        self.surface.scrolling()

    def process_draw(self):
        self.game.screen.blit(self.surface.screen, (0, self.surface.scroll))
        super().process_draw()
        self.back_button.draw(self.game.screen)
