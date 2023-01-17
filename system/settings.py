"""Класс, работающий с настройками. Не отображается"""
import json
import os.path
from constants import SETTINGS_PATH


class Settings:
    wasd = 1
    arrows = 0
    save_file = SETTINGS_PATH
    DEFAULT_SETTINGS = {
        'keys': 1,
        'music': True,
        'sound': True,
        'animation': True,
        'debug': False,
        'walls_off': False
    }

    def __init__(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as fp:
                self.storage = json.load(fp)
        else:
            self.storage = Settings.DEFAULT_SETTINGS

    def __del__(self):
        self.write_to_file()

    @property
    def keys(self):
        return self.storage['keys']

    @property
    def music(self):
        return self.storage['music']

    @property
    def sound(self):
        return self.storage['sound']

    @property
    def animation(self):
        try:
            self.storage['animation']
        except KeyError:
            self.storage['animation'] = self.DEFAULT_SETTINGS['animation']
        return self.storage['animation']

    @property
    def debug(self):
        try:
            self.storage['debug']
        except KeyError:
            self.storage['debug'] = self.DEFAULT_SETTINGS['debug']
        return self.storage['debug']

    @property
    def walls_off(self):
        try:
            self.storage['walls_off']
        except KeyError:
            self.storage['walls_off'] = self.DEFAULT_SETTINGS['walls_off']
        return self.storage['walls_off']

    def update_character_keys(self, character=None):
        if character:
            character.movement_keys(self.keys)

    def write_to_file(self):
        with open(self.save_file, 'w') as fp:
            json.dump(self.storage, fp, indent=4)

    def change_keys(self, key):
        self.storage['keys'] = key

    def music_change(self):
        self.storage['music'] = not self.music

    def sound_change(self):
        self.storage['sound'] = not self.sound

    def anim_change(self):
        self.storage['animation'] = not self.animation

    def debug_change(self):
        self.storage['debug'] = not self.debug

    def walls_change(self):
        self.storage['walls_off'] = not self.walls_off
