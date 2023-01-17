"""Класс сцены с уровнем"""
import pygame
from objects.ghost_objects.blinky import Blinky
from objects.ghost_objects.clyde import Clyde
from objects.ghost_objects.inky import Inky
from objects.ghost_objects.pinky import Pinky
from objects.text import TextObject
from constants import FONT, BLACK
from objects.lives import Lives
from objects.field import Field
from objects.pacman import Pacman
from scenes.base import BaseScene
from objects.cherry import Cherry


class GameScene(BaseScene):
    start = False

    def __init__(self, game, score):
        super().__init__(game)
        self.field = Field(self.game, 10, 10, 'maps/original.txt')
        self.objects.append(self.field)
        self.pacman = Pacman(self.game, self.field, 18 * 15, 18 * 24)
        self.objects.append(self.pacman)
        self.ghosts = [Blinky(self.game, self.field), Clyde(self.game, self.field), Pinky(self.game, self.field), Inky(self.game, self.field)]
        self.objects += self.ghosts
        self.demo_lives = Lives(self.game, 10, game.size[1] - 30, 23, 25)
        self.objects.append(self.demo_lives)
        self.cherry = Cherry(game)
        self.objects.append(self.cherry)
        self.score = score
        self.ghost_bounty = 200

    def process_logic(self):
        if not self.start:
            return
        super().process_logic()
        # логика призраков
        for ghost in self.ghosts:
            if ghost.collide_with(self.pacman):
                if not ghost.frightened_is_active:
                    self.demo_lives.damage()
                    self.pacman.reset_position()
                    self.game.sounds.sounds['death'].play()
                    for g in self.ghosts:
                        g.reset()
                else:
                    ghost.reset()
                    self.score.increase_on(self.ghost_bounty)
                    self.ghost_bounty *= 2
        # работа с вишенкой
        if self.field.seeds_count == 170 or self.field.seeds_count == 70:
            self.cherry.activate()
        if self.cherry.is_on_field and self.cherry.collide_with(self.pacman):
            self.score.increase_on(self.cherry.POINTS)
            self.cherry.is_on_field = False
            self.game.sounds.sounds['eat_fruit'].play()
        # условие победы
        if self.field.seeds_count == 0:
            self.game.set_scene(self.game.SCENE_GAMEOVER)
            self.game.sounds.stop()
            self.game.sounds.sounds['extend'].play()
            self.reset()

    def process_event(self, event):
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if not self.start:
            if event.type == pygame.KEYDOWN:
                self.start = True
                self.game.sounds.mus_change()
        if event.key == pygame.K_ESCAPE:
            self.game.set_scene(self.game.SCENE_PAUSE)
        if event.key == pygame.K_p:
            self.game.set_scene(self.game.SCENE_PAUSE)
        if event.key == pygame.K_z:
            self.game.settings.debug_change()
        if event.key == pygame.K_x:
            self.game.settings.walls_change()

    def process_draw(self):
        super().process_draw()
        text1 = TextObject(self.game, 600, 100, '1UP', pygame.Color('white'))
        text2 = TextObject(self.game, 600, 140, str(self.score.current_points()), pygame.Color('white'))
        text3 = TextObject(self.game, self.game.width // 2, self.game.height // 2 - 60,
                           'Нажмите любую клавишу чтобы продолжить', pygame.Color('red'), FONT)
        text1.process_draw()
        text2.process_draw()
        pygame.draw.rect(self.game.screen, BLACK, (10, 18 * 13 + 10, 36, 54))
        pygame.draw.rect(self.game.screen, BLACK, (26 * 18 + 10, 18 * 13 + 10, 36, 54))
        if not self.start:
            text3.process_draw()

    def on_activate(self):
        super().on_activate()
        self.pacman.movement_keys()
        self.start = False
        self.game.sounds.mus_change(2)

    def reset(self):
        self.score.reset()
        self.field.load_map()
        self.pacman.reset_position()
        self.cherry.is_on_field = False
        for ghost in self.ghosts:
            ghost.reset()
