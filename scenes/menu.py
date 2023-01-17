"""Класс главного меню"""
from constants import BLACK
from objects.button import ButtonObject
from scenes.base import BaseScene
from objects.image import ImageObject
from scenes.animation import AnimationScene
import pygame


class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.surface = pygame.Surface((1000, 750))
        self.surface.set_alpha(0)
        self.surface.fill((0, 0, 0))
        inscription = ImageObject(game, 'images/menu_inscription.png', 150, -15)
        self.objects.append(inscription)
        self.objects.append(AnimationScene(game, self.surface))

        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 3 + 65, 200, 50,
                BLACK, self.start_game, text='Запуск игры'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 2 + 20, 200, 50,
                BLACK, self.open_settings, text='Настройки'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height - 225, 200, 50,
                BLACK, self.open_highscore, text='Рекорды'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height - 170, 200, 50,
                BLACK, self.open_about, text='Об игре'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height - 115, 200, 50,
                BLACK, self.game.exit_game, text='Выход'
            )
        )

    def on_deactivate(self):
        super().on_deactivate()
        self.objects[1].on_deactivate()

    def on_activate(self):
        super().on_activate()
        self.objects[1].on_activate()
        self.surface.set_alpha(0)

    def process_draw(self):
        super().process_draw()
        self.game.screen.blit(self.surface, (0, 0))

    def start_game(self):
        self.game.scenes[self.game.SCENE_GAME].reset()
        if self.game.settings.animation:
            self.objects[1].start = True
            self.game.sounds.sounds['waka waka'].play(-1)
            self.game.sounds.mus_change(1)
        else:
            self.game.set_scene(self.game.SCENE_GAME)

    def open_settings(self):
        self.game.set_scene(self.game.SCENE_SETTINGS)

    def open_highscore(self):
        self.game.set_scene(self.game.SCENE_HIGHSCORE)

    def open_about(self):
        self.game.set_scene(self.game.SCENE_ABOUT)
