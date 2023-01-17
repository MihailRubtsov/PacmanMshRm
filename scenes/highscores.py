"""Класс сцены с рекордами. Отображает таблицу"""
from scenes.base import BaseScene
from system.highscore import Highscore
from objects.text import TextObject
from objects.button import ButtonObject
from constants import BLACK, GREEN, RED
import pygame


class HighscoreScene(BaseScene):
    def __init__(self, game, score):
        super().__init__(game)
        self.game = game
        self.highscore = Highscore()
        self.score = score
        self.arr = self.highscore.highscores
        self.objects.append(TextObject(self.game, self.game.width // 2, 30, 'Таблица рекордов', GREEN))
        self.objects.append(ButtonObject(self.game, self.game.width // 2 - 300, self.game.height - 100,
                                         250, 50, BLACK, self.back_to_menu, 'Назад в меню'))
        self.objects.append(ButtonObject(self.game, self.game.width // 2 + 50, self.game.height - 100,
                                         300, 50, BLACK, self.reset_highscores, 'Сброс результатов'))
        self.objects.append(TextObject(self.game, self.game.width // 2 - 200, 90, 'Имя:', RED))
        self.objects.append(TextObject(self.game, self.game.width // 2 + 200, 90, 'Очки:', RED))

    def back_to_menu(self):
        self.game.set_scene(self.game.SCENE_MENU)
        self.game.scenes[self.game.SCENE_GAME].reset()
        self.highscore.save_to_file()

    def reset_highscores(self):
        self.highscore.clean_all_results()

    def add(self):
        self.highscore.add_new_result(self.game.player_name, self.score.current_points())
        self.highscore.save_to_file()

    def update(self):
        self.highscore.load_from_file()
        self.arr = self.highscore.highscores
        self.objects = self.objects[:5]  # все результаты удаляются из массива и читаются из файла заного
        for i in range(len(self.arr)):
            self.objects.append(TextObject(self.game, self.game.width // 2 - 200, i*38 + 140, self.arr[i][0], RED))
            self.objects.append(TextObject(self.game, self.game.width // 2 + 200, i*38 + 140, str(self.arr[i][1]), RED))

    def process_logic(self):
        self.update()

    def process_event(self, event):
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            self.game.set_scene(self.game.SCENE_MENU)
