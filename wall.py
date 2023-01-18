"""Классы стены и пустого (чёрного) объекта"""
import pygame
from constants import BLUE, BLACK
from objects.base import DrawableObject


class Wall(DrawableObject):
    WIDTH = 18

    def __init__(self, game, x, y):
        super().__init__(game)
        self.move(x, y)
        self.rect.width = self.WIDTH
        self.rect.height = self.WIDTH

    def process_draw(self):
        if not self.game.settings.walls_off:
            pygame.draw.rect(self.game.screen, BLUE, self.rect, 0)
        else:
            pygame.draw.rect(self.game.screen, BLACK, self.rect, 0)


class Empty(DrawableObject):
    WIDTH = 18

    def __init__(self, game, x, y):
        super().__init__(game)
        self.move(x, y)
        self.rect.width = self.WIDTH
        self.rect.height = self.WIDTH

    def process_draw(self):
        pygame.draw.rect(self.game.screen, BLACK, self.rect, 0)


class TeleportWall(Wall):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def get_object_list_with_collisions(self, objects):
        return self.rect.collidelist(objects)
