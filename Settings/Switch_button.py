"""Кнопка-переключатель"""
import pygame
from objects.Settings.standart_button import Button


class Switch_button(Button):
    def __init__(self, x, y, image, image_pressed, scale, function=None):
        width = image.get_width()
        height = image.get_height()
        super().__init__(x, y, width, height, image, scale, function)
        self.image_pressed = pygame.transform.scale(image_pressed, (int(width * scale), int(height * scale)))
        self.other = None

    def off(self):
        self.switch = False

    def connect(self, button):
        self.other = button
        button.other = self

    def click(self):
        super().click()
        self.switch = True
        self.other.off()

    def is_clicked(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.click()

        super().is_clicked()

    def draw(self, screen):
        self.is_clicked()
        img = {
            True: self.image_pressed,
            False: self.image
        }
        self.is_clicked()
        screen.blit(img[self.switch], (self.rect.x, self.rect.y))
