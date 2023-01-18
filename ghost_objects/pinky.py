"""Скрипт розового призрака"""
from objects.ghosts import Ghost


class Pinky(Ghost):
    filename = "images/ghosts/pinky/pinky.png"
    IMAGES = {
        Ghost.LEFT: 'images/ghosts/pinky/left.png',
        Ghost.UP: 'images/ghosts/pinky/up.png',
        Ghost.DOWN: 'images/ghosts/pinky/down.png',
        Ghost.RIGHT: 'images/ghosts/pinky/right.png'
    }

    def __init__(self, game, field, x=10 + 18 * 14, y=10 + 18 * 14):
        super().__init__(self.filename, game, field, x, y)
        self.x, self.y = x, y
        self.aim_default_x, self.aim_default_y = 10 - 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    def reset(self):
        super().__init__(self.filename, self.game, self.field, self.x, self.y)
        self.aim_default_x, self.aim_default_y = 10 - 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    def change_state(self):
        if self.state == self.STAY_IN:
            self.state = self.BEGIN
            self.direction = self.UP
        else:
            super().change_state()

    # позиция берётся из класса пакмана
    def choose_aim_position(self):
        if self.state == self.HUNT:
            pacman = self.game.scenes[self.game.current_scene_index].pacman
            pacman_directions = {pacman.LEFT: [-4, 0], pacman.RIGHT: [4, 0], pacman.UP: [-4, -4], pacman.DOWN: [0, 4]}
            self.aim_x, self.aim_y = pacman.rect.x + 18 * pacman_directions[pacman.direction][0], \
                                     pacman.rect.y + 18 * pacman_directions[pacman.direction][1]
        else:
            super().choose_aim_position()

    def process_draw(self):
        super().process_draw((255, 99, 178))
