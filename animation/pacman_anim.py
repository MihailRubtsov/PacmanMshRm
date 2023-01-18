import pygame
from objects.pacman import Pacman


class AnimPacman(Pacman):
    def __init__(self, game, scene, seed=300, x=450, y=300):
        super().__init__(game, None, x, y)
        self.seed = seed
        self.scene = scene

    def check_borders(self):
        pass

    def step(self, back=False):
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
            self.animation()
            self.step()
            if self.rect.centerx >= self.seed + 10:
                self.scene.objects.pop(0)
                self.ate()
            if self.rect.centerx <= 400:
                self.scene.surface.set_alpha(self.scene.surface.get_alpha() + 2)
            self.end()

    def ate(self):
        self.direction = self.LEFT
        self.scene.fear = True
        self.game.sounds.mus_change(2)

    def end(self):
        if self.direction == self.LEFT and self.rect.centerx <= -10:
            pygame.time.wait(150)
            self.game.set_scene(self.game.SCENE_GAME)
