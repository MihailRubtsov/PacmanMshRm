"""Класс с жизнями"""
import pygame
from objects.image import ImageObject


class Lives(ImageObject):
    filename = 'images/pacman/right/1.png'
    image = pygame.image.load(filename)

    def __init__(self, game, x=300, y=300, w=50, h=50, m=10, lives=3):
        super().__init__(game)
        self.game = game
        self.lives = lives
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.margin = m
        self.image = pygame.transform.scale(self.image, (w, h))

    def reset(self):
        self.game.sounds.sounds['death'].play()
        self.lives = 3

    def is_alive(self):
        if self.lives > 0:
            return True
        return False

    def damage(self):
        self.lives -= 1

    def process_logic(self):
        if not self.is_alive():
            self.game.set_scene(self.game.SCENE_GAMEOVER)
            self.reset()

    def process_draw(self):
        for i in range(self.lives):
            rect = self.image.get_rect()
            rect.x = self.x + i * self.width + i * self.margin
            rect.y = self.y
            rect.width = self.width
            rect.height = self.height
            self.game.screen.blit(self.image, rect)
