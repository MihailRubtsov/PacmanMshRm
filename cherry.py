"""Класс вишенки, которая появляется на сцене при съедении нескольких зёрен"""
from datetime import datetime
import pygame
from objects.image import ImageObject


class Cherry(ImageObject):
    filename = 'images/cherry.png'
    image = pygame.image.load(filename)
    POINTS = 200

    def __init__(self, game, x=18 * 15, y=18 * 18, seconds_to_hide=20):
        super().__init__(game, None, x, y)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.start = datetime.now()
        self.seconds = seconds_to_hide
        self.is_on_field = False

    def activate(self):
        self.start = datetime.now()
        self.is_on_field = True

    def collide_with(self, other):
        return self.rect.colliderect(other.rect)

    def process_logic(self):
        if self.is_on_field:
            if (datetime.now() - self.start).seconds >= self.seconds:
                self.is_on_field = False

    def process_draw(self):
        if self.is_on_field:
            self.game.screen.blit(self.image, self.rect)
