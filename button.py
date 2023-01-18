import pygame
from third_party.button import Button
from constants import BLACK, WHITE, FONT
from objects.base import DrawableObject


class ButtonObject(DrawableObject):
    BUTTON_STYLE = {
        "hover_color": BLACK,
        "clicked_color": BLACK,
        "clicked_font_color": WHITE,
        "hover_font_color": WHITE,
        "font": pygame.font.Font(FONT, 24)
    }

    def __init__(self, game, x, y, width, height, color, function, text):
        super().__init__(game)
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.button = Button((x, y, width, height), color, function, text=text, **self.BUTTON_STYLE)

    def process_event(self, event):
        self.button.check_event(event)

    def process_draw(self):
        self.button.update(self.game.screen)
