import pygame

from objects.base import DrawableObject


class TextObject(DrawableObject):

    def __init__(self, game, x, y, text, color, font=None, size=None):
        super().__init__(game)
        self.color = color
        self.y = y
        self.x = x
        if font:
            self.size = 22 if size is None else size
            self.font = pygame.font.Font(font, self.size)
        else:
            self.size = 30 if size is None else size
            self.font = pygame.font.SysFont('Comic Sans MS', self.size, True)
        self.update_text(text)

    def update_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.move_center(self.x, self.y)

    def process_draw(self):
        self.game.screen.blit(self.surface, self.rect)
