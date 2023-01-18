"""Скрипт оранжевого призрака"""
from objects.ghosts import Ghost


class Clyde(Ghost):
    filename = "images/ghosts/clyde/clyde.png"
    IMAGES = {
        Ghost.LEFT: 'images/ghosts/clyde/left.png',
        Ghost.UP: 'images/ghosts/clyde/up.png',
        Ghost.DOWN: 'images/ghosts/clyde/down.png',
        Ghost.RIGHT: 'images/ghosts/clyde/right.png'
    }

    def __init__(self, game, field, x=10 + 18 * 12, y=10 + 18 * 14):
        super().__init__(self.filename, game, field, x, y)
        self.x, self.y = x, y
        self.aim_default_x, self.aim_default_y = 10 - 18 * 50, 10 + 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 14, 10 + 18 * 11

    def reset(self):
        super().__init__(self.filename, self.game, self.field, self.x, self.y)
        self.aim_default_x, self.aim_default_y = 10 - 18 * 50, 10 + 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 14, 10 + 18 * 11

    def change_state(self):
        if self.state == self.STAY_IN:
            seed_count = self.field.get_seed_count()
            if seed_count / self.initial_seed_count < 2 / 3:
                self.state = self.BEGIN
                self.direction = self.UP
        else:
            super().change_state()

    # позиция берётся из класса пакмана
    def choose_aim_position(self):
        if self.state == self.HUNT:
            pacman = self.game.scenes[self.game.current_scene_index].pacman
            distance = ((pacman.rect.x - self.rect.x) ** 2 + (pacman.rect.y - self.rect.y) ** 2) ** 0.5

            if distance > 8 * 18:
                self.aim_x, self.aim_y = pacman.rect.x, pacman.rect.y
            else:
                self.aim_x, self.aim_y = self.aim_default_x, self.aim_default_y
        else:
            super().choose_aim_position()

    def process_draw(self):
        super().process_draw((255, 161, 1))
