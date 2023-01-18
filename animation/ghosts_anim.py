from objects.image import ImageObject
import pygame


class AnimGhost(ImageObject):
    RIGHT = 0
    LEFT = 1

    def __init__(self, game, scene, filename, x, y):
        super().__init__(game, filename, x, y)
        self.image = pygame.transform.scale(self.image, (18, 18))
        self.normal_image = pygame.image.load(filename)
        self.image_fear = pygame.image.load('images/ghosts/scared.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.direction = self.RIGHT
        self.scene = scene

    def step(self):
        directions = {
            self.RIGHT: [2, 0],
            self.LEFT: [-3, 0],
            }
        self.move_center(
            self.rect.centerx + directions[self.direction][0],
            self.rect.centery + directions[self.direction][1]
        )

    def process_logic(self):
        if self.scene.start:
            self.step()
            if self.scene.fear:
                self.direction = self.LEFT
                self.image = self.image_fear
                self.image = pygame.transform.scale(self.image, (20, 20))
