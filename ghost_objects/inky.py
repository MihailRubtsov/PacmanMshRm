"""Скрипт голубого призрака"""
from objects.ghosts import Ghost


class Inky(Ghost):
    filename = "images/ghosts/inky/inky.png"
    IMAGES = {
        Ghost.LEFT: 'images/ghosts/inky/left.png',
        Ghost.UP: 'images/ghosts/inky/up.png',
        Ghost.DOWN: 'images/ghosts/inky/down.png',
        Ghost.RIGHT: 'images/ghosts/inky/right.png'
    }

    def __init__(self, game, field, x=10 + 18 * 16, y=10 + 18 * 14):
        super().__init__(self.filename, game, field, x, y)
        self.x, self.y = x, y
        self.aim_default_x, self.aim_default_y = 10 + 18 * 50, 10 + 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 14, 10 + 18 * 11

    def reset(self):
        super().__init__(self.filename, self.game, self.field, self.x, self.y)
        self.aim_default_x, self.aim_default_y = 10 + 18 * 50, 10 + 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 14, 10 + 18 * 11

    def change_state(self):
        if self.state == self.STAY_IN:
            seed_count = self.field.get_seed_count()
            if self.initial_seed_count - seed_count >= 30:
                self.state = self.BEGIN
                self.direction = self.UP
        else:
            super().change_state()

    # позиция берётся из класса пакмана и класса блинки
    def choose_aim_position(self):
        if self.state == self.HUNT:
            pacman = self.game.scenes[self.game.current_scene_index].pacman
            blinky = self.game.scenes[self.game.current_scene_index].ghosts[0]

            pacman_directions = {pacman.LEFT: [-2, 0], pacman.RIGHT: [2, 0], pacman.UP: [-2, -2], pacman.DOWN: [0, 2]}
            delta = [(pacman.rect.x + 18 * pacman_directions[pacman.direction][0] - blinky.rect.x) * 2,
                     (pacman.rect.y + 18 * pacman_directions[pacman.direction][1] - blinky.rect.y) * 2]

            self.aim_x, self.aim_y = blinky.rect.x + delta[0], blinky.rect.y + delta[1]
        else:
            super().choose_aim_position()

    def process_draw(self):
        super().process_draw((0, 254, 254))
