"""Кнопка формата квадрат с галочкой"""
import pygame
from objects.Settings.standart_button import Button


class Check_button(Button):
    def __init__(self, x, y, width, height, image, scale=1, text='yes', function=None):
        super().__init__(x, y, width, height, image, scale, function)
        self.switch = True
        self.width = width
        self.height = height
        self.x, self.y = x, y
        self.text = text

    def click(self):
        super().click()
        self.switch = not self.switch

    def is_clicked(self):
        pos = pygame.mouse.get_pos()

        if self.x < pos[0] < self.x + self.width * self.scale:
            if self.y < pos[1] < self.y + self.height * self.scale:
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.click()

        super().is_clicked()

    def get_text(self):
        font = pygame.font.SysFont('dejavuserif', 30 * self.scale)
        follow = font.render(self.text, True, (111, 111, 111), (0, 0, 0))
        return follow

    def draw(self, screen):
        self.is_clicked()

        if self.switch:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.get_text(), (self.x + 40 * self.scale, self.y - 6 * self.scale))
        pygame.draw.rect(screen, (88, 88, 88), (self.x, self.y, 30 * self.scale, 30 * self.scale), 3 * self.scale)
