import pygame.mixer as mixer
import os


class Sounds:
    sounds = {}

    def __init__(self, game):
        for items in os.walk("sounds"):
            for file in items[2]:
                self.add_sound(file)
        self.game = game
        self.sets = self.game.settings
        self.mus_switch()

    def add_sound(self, file):
        ext = file.split('.')[-1]
        name = file.replace('.'+ext, '')
        self.sounds[name] = mixer.Sound('sounds/' + file)

    def mus_change(self, mod=0):
        if self.sets.music:
            mixer.music.stop()

            if self.game.current_scene_index == 0:
                if mod == 0:
                    mixer.music.load('sounds/game_start.wav')
                    mixer.music.play(1)
                elif mod == 1:
                    mixer.music.load('sounds/siren.wav')
                    mixer.music.play(-1)
                elif mod == 2:
                    mixer.music.load('sounds/power_pellet.wav')
                    mixer.music.play(-1)

            elif self.game.current_scene_index == 1:
                if mod == 0:
                    mixer.music.load('sounds/siren.wav')
                elif mod == 1:
                    mixer.music.load('sounds/power_pellet.wav')
                elif mod == 2:
                    mixer.music.load('sounds/game_start.wav')
                mixer.music.play(-1)

            elif self.game.current_scene_index == 6:
                mixer.music.load('sounds/intermission.wav')
                mixer.music.play(-1)

            elif self.game.current_scene_index == 8:
                mixer.music.load('sounds/about.wav')
                mixer.music.play(-1)

    def stop(self):
        for sound in self.sounds.values():
            sound.stop()
        mixer.music.stop()

    def mus_switch(self):
        if not self.game.settings.sound:
            for sound in self.sounds.values():
                sound.set_volume(0)
        else:
            for sound in self.sounds.values():
                sound.set_volume(0.5)
        if not self.sets.music:
            mixer.music.stop()
