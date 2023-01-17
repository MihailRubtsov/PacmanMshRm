"""Класс сцены с вводом имени. Имя не может содержать пробел"""
import pygame
from constants import WHITE
from objects.text import TextObject
from objects.kursor import KursorObject
from scenes.base import BaseScene


class EnternameScene(BaseScene):
    MAX_LEN = 10

    def __init__(self, game):
        super().__init__(game)
        self.objects.append(TextObject(self.game, self.game.width // 2, self.game.height // 2 - 200, 'INPUT YOUR NAME', WHITE))
        self.objects.append(TextObject(self.game, self.game.width // 2, self.game.height // 2, '', WHITE))
        self.objects.append(TextObject(self.game, self.game.width // 2, self.game.height // 2 + 200, 'PRESS ENTER TO CONTINUE', WHITE))
        self.objects.append(KursorObject(self.game, self.game.width // 2 + self.objects[1].rect.w + 2, self.game.height // 2, '_', WHITE))

    def process_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_RETURN:
            if len(self.game.player_name) == 0:
                self.game.player_name = 'NO_NAME'
            self.game.set_scene(self.game.SCENE_HIGHSCORE)
            self.game.scenes[self.game.SCENE_HIGHSCORE].add()
        elif event.key == pygame.K_BACKSPACE:
            if len(self.game.player_name) > 0:
                self.game.player_name = self.game.player_name[:-1]
                self.objects[1].update_text(self.game.player_name)
                self.objects[3].move_center(self.objects[1].rect.right + self.objects[3].rect.w // 2, self.game.height // 2)
        else:
            if len(self.game.player_name) < self.MAX_LEN:
                if event.unicode != ' ':  # имя не должно содержать пробел, так как это ломает работу кода с сохранением рекордов
                    self.game.player_name += event.unicode
            self.objects[1].update_text(self.game.player_name)
            self.objects[3].move_center(self.objects[1].rect.right + self.objects[3].rect.w // 2, self.game.height // 2)

    def process_draw(self):
        for object in self.objects:
            object.process_draw()
