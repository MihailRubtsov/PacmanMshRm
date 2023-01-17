"""Основной класс игры"""
import pygame
from constants import BLACK, SAVE_PATH
from scenes.about import AboutScene
from system.score import Score
from scenes.game import GameScene
from scenes.gameover import GameOverScene
from scenes.menu import MenuScene
from scenes.highscores import HighscoreScene
from scenes.pause import PauseScene
from scenes.entername import EnternameScene
from scenes.settings import SettingsScene
from system.settings import Settings
from scenes.first_time_settings import FirstTimeSettingsScene
from system.sound_manager import Sounds


class Game:
    size = width, height = 800, 600
    SCENE_MENU = 0
    SCENE_GAME = 1
    SCENE_GAMEOVER = 2
    SCENE_PAUSE = 3
    SCENE_ENTERNAME = 4
    SCENE_SETTINGS = 5
    SCENE_HIGHSCORE = 6
    SCENE_START_SETTINGS = 7
    SCENE_ABOUT = 8
    current_scene_index = SCENE_START_SETTINGS

    def __init__(self):
        check_files()
        self.screen = pygame.display.set_mode(self.size)
        self.game_over = False
        self.player_name = ''
        self.score = Score()
        self.settings = Settings()
        self.sounds = Sounds(self)
        self.scenes = [
            MenuScene(self),
            GameScene(self, self.score),
            GameOverScene(self),
            PauseScene(self),
            EnternameScene(self),
            SettingsScene(self),
            HighscoreScene(self, self.score),
            FirstTimeSettingsScene(self),
            AboutScene(self)
        ]

    @staticmethod
    def exit_button_pressed(event):
        return event.type == pygame.QUIT

    @staticmethod
    def exit_hotkey_pressed(event):
        return event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL and event.key == pygame.K_q

    def process_exit_events(self, event):
        if Game.exit_button_pressed(event) or Game.exit_hotkey_pressed(event):
            self.exit_game()

    def process_all_events(self):
        for event in pygame.event.get():
            self.process_exit_events(event)
            self.scenes[self.current_scene_index].process_event(event)

    def process_all_logic(self):
        self.scenes[self.current_scene_index].process_logic()

    def set_scene(self, index):
        self.scenes[self.current_scene_index].on_deactivate()
        self.current_scene_index = index
        self.scenes[self.current_scene_index].on_activate()

    def process_all_draw(self):
        self.screen.fill(BLACK)
        self.scenes[self.current_scene_index].process_draw()
        pygame.display.flip()

    def main_loop(self):
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            pygame.time.wait(10)

    def exit_game(self):
        print('Bye bye')
        self.game_over = True


# проверка файла с рекордами
def check_files():
    try:
        f = open(SAVE_PATH, 'r')
        int(f.readline()[0])
        f.close()
    except IndexError:
        f = open(SAVE_PATH, 'w')
        f.write("0")
    except ValueError:
        f = open(SAVE_PATH, 'w')
        f.write("0")
    except FileNotFoundError:
        with open(SAVE_PATH, 'w') as f:
            f.write('0')
