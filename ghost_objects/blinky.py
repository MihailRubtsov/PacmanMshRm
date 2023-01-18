"""Скрипт красного призрака"""
from objects.ghosts import Ghost


class Blinky(Ghost):
    filename = 'images/ghosts/blinky/up.png'
    IMAGES = {
        Ghost.LEFT: 'images/ghosts/blinky/left.png',
        Ghost.UP: 'images/ghosts/blinky/up.png',
        Ghost.DOWN: 'images/ghosts/blinky/down.png',
        Ghost.RIGHT: 'images/ghosts/blinky/right.png'
    }
    cruise_elroy_is_active = False

    def __init__(self, game, field, x=10 + 18 * 14, y=10 + 18 * 11):
        super().__init__(self.filename, game, field, x, y)
        self.x, self.y = x, y
        self.aim_default_x, self.aim_default_y = 10 + 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    def reset(self):
        super().__init__(self.filename, self.game, self.field, self.x, self.y)
        self.aim_default_x, self.aim_default_y = 10 + 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    # режим, который имеет только этот призрак
    def check_cruise_elroy(self):
        # Здесь необходимый процент - 25, при необходимости можно изменить
        seed_count = self.field.get_seed_count()
        if seed_count / self.initial_seed_count <= 0.25:
            self.cruise_elroy_is_active = True

    def change_state(self):
        if self.state == self.STAY_IN:
            self.state = self.BEGIN
            self.direction = self.UP
        else:
            super().change_state()

    # позиция берётся из класса пакмана
    def choose_aim_position(self):
        if not self.cruise_elroy_is_active:
            self.check_cruise_elroy()

        if self.state == self.WANDER:
            if self.cruise_elroy_is_active:
                pacman = self.game.scenes[self.game.current_scene_index].pacman
                self.aim_x, self.aim_y = pacman.rect.x, pacman.rect.y
            else:
                self.aim_x, self.aim_y = self.aim_default_x, self.aim_default_y
        elif self.state == self.HUNT:
            pacman = self.game.scenes[self.game.current_scene_index].pacman
            self.aim_x, self.aim_y = pacman.rect.x, pacman.rect.y
        else:
            super().choose_aim_position()

    def process_draw(self):
        super().process_draw((227, 0, 27))
