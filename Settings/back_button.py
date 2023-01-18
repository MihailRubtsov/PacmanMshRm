"""Кнопка возврата. Находится вверху слева"""
import pygame as pg
from objects.Settings.standart_button import Button


class BackButton(Button):
    def __init__(self, x, y, game, function=None, text='Back'):
        self.x, self.y = x, y
        self.clicked = False
        self.hovered = False
        self.game = game
        self.function = function
        self.wait = False
        self.text = text
        self.padding = 100

    def get_text(self, color):
        font = pg.font.SysFont('arial', 30)
        follow = font.render(self.text, False, color, (0, 0, 0))
        return follow

    def draw_button(self, screen, color):
        pg.draw.polygon(screen, color, ((self.x + 10, self.y), (self.x + 20, self.y + 10), (self.x, self.y),
                                        (self.x + 20, self.y - 10), (self.x + 10, self.y)))
        screen.blit(self.get_text(color), (30, 6))
        pg.draw.rect(screen, color, (self.x - 5, self.y - 20, self.padding, 40), 2)

    def waiting(self):
        if self.wait:
            if not self.clicked:
                self.wait = False
                self.click()

    def click(self):
        if self.function is not None:
            self.function()

    def is_clicked(self):
        pos = pg.mouse.get_pos()
        self.hovered = False

        if self.x - 5 < pos[0] < self.x + self.padding - 5:
            if self.y - 20 < pos[1] < self.y + 20:
                self.hovered = True
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.wait = True

        super().is_clicked()

    def draw(self, screen):
        self.waiting()
        self.is_clicked()
        if not self.hovered:
            self.draw_button(screen, (88, 88, 88))
        else:
            self.draw_button(screen, (255, 255, 255))
            surface = screen.convert_alpha()
            surface.fill([0, 0, 0, 0])
            if not self.clicked:
                pg.draw.rect(surface, (88, 88, 88, 150), (self.x - 5, self.y - 20, self.padding + 1, 41))
            screen.blit(surface, (0, 0))
