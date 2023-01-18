"""Классы обычного и большого зерна"""
import pygame
from constants import WHITE
from objects.base import DrawableObject
from objects.image import ImageObject


class Seed(DrawableObject):
    POINTS = 10
    RADIUS = 3
    WIDTH = 18
    COLOR = WHITE

    def __init__(self, game, x=0, y=0):
        super().__init__(game)
        self.rect.width = self.WIDTH
        self.rect.height = self.WIDTH
        self.move(x, y)

    def process_draw(self):
        pygame.draw.circle(self.game.screen, self.COLOR, self.rect.center, self.RADIUS)

    def get_object_list_with_collisions(self, objects):
        return self.rect.collidelist(objects)


class BigSeed(ImageObject):
    POINTS = 50
    filename = 'images/big_seed.png'
    CELL_WIDTH = 18

    def __init__(self, game, x, y):
        super().__init__(game, None, x, y)
        self.image_width = self.rect.width
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        self.game.screen.blit(
            self.image,
            (
                self.rect.centerx - self.image_width // 2,
                self.rect.centery - self.image_width // 2
            )
        )

    def get_object_list_with_collisions(self, objects):
        return self.rect.collidelist(objects)
