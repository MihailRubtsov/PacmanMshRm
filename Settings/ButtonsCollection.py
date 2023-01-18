"""Здесь находятся все кнопки и нужные им функции, используемые в сцене настроек"""
from objects.Settings.Switch_button import Switch_button
from objects.Settings.check_mark import Check_button
from objects.Settings.back_button import BackButton
import pygame as pg


class ButtonsColection:
    def __init__(self, game):
        self.game = game
        self.buttons = self.create_buttons()
        self.prev_settings()

    def create_buttons(self):
        width, height = self.game.width, self.game.height
        scale = width / 800

        arrows = new_button(width / 2 + 40 * scale, 75, 'images/settings/arrows.png',
                            'images/settings/arrows_p.png', scale, self.function_arrows)
        wasd = new_button(width / 2 - 250 * scale, 75, 'images/settings/WASD.png',
                          'images/settings/WASD_p.png', scale, self.function_wasd)
        arrows.connect(wasd)

        mus_button = new_checkmark(30, height * 0.7, 'images/settings/ok.png',
                                   scale, 'музыка вкл/выкл', self.function_checkmark_music)
        sound_button = new_checkmark(30, height * 0.8, 'images/settings//ok.png',
                                     scale, 'звуки вкл/выкл', self.function_checkmark_sound)
        anim_button = new_checkmark(30, height * 0.9, 'images/settings//ok.png',
                                    scale, 'анимация вкл/выкл', self.function_checkmark_anim)
        targets_button = new_checkmark(width / 2 + 40, height * 0.74, 'images/settings//ok.png',
                                       scale, 'debug mod', self.function_checkmark_debug_mod)
        walls_button = new_checkmark(width / 2 + 40, height * 0.84, 'images/settings//ok.png',
                                     scale, 'прозрачные стены', self.function_checkmark_walls)

        back_button = BackButton(5, 20, self.game, self.function_back, text='Принять')
        back_button.padding = 150
        buttons = [wasd, arrows, mus_button, sound_button, anim_button, targets_button, walls_button,
                   back_button]  # back_button всегда должна быть последней в этом списке (нужно для сцены с преднастройками)
        return buttons

    def function_back(self):
        self.game.set_scene(self.game.SCENE_MENU)
        self.game.settings.write_to_file()

    # Здесь поместить функцию для смены на WASD
    def function_wasd(self):
        self.game.settings.change_keys(self.game.settings.wasd)

    # Здесь поместить функцию для смены на стрелочки
    def function_arrows(self):
        self.game.settings.change_keys(self.game.settings.arrows)

    # Здесь поместить функцию включения/выключения музыки
    def function_checkmark_music(self):
        self.game.settings.music_change()

    # Здесь поместить функцию включения/выключения звуков
    def function_checkmark_sound(self):
        self.game.settings.sound_change()

    # Функция включения и выключения анимации
    def function_checkmark_anim(self):
        self.game.settings.anim_change()

    def function_checkmark_debug_mod(self):
        self.game.settings.debug_change()

    def function_checkmark_walls(self):
        self.game.settings.walls_change()

    def prev_settings(self):
        # Управление на WASD
        self.buttons[0].switch = self.game.settings.keys
        # Управление на Стрелочки
        self.buttons[1].switch = not self.game.settings.keys
        # Музыка
        self.buttons[2].switch = self.game.settings.music
        # Звуки
        self.buttons[3].switch = self.game.settings.sound
        # Анимация
        self.buttons[4].switch = self.game.settings.animation
        # Debug mod
        self.buttons[5].switch = self.game.settings.debug
        # Отображение стен
        self.buttons[6].switch = self.game.settings.walls_off


def new_button(x, y, image_path, pressed_image_path, scale, function):
    img = pg.image.load(image_path).convert_alpha()
    img_pressed = pg.image.load(pressed_image_path).convert_alpha()

    butt = Switch_button(x, y, img, img_pressed, 0.3 * scale, function)
    return butt


def new_checkmark(x, y, img_path, scale, text, function):
    img = pg.image.load(img_path).convert_alpha()
    checkmark = Check_button(x, y, 30, 30, img, int(scale), text, function)
    return checkmark
