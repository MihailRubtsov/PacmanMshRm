import game


class BaseScene:
    def __init__(self, game):
        self.game = game
        self.objects = []

    def on_activate(self):
        self.game.sounds.mus_change()

    def process_event(self, event):
        for object in self.objects:
            object.process_event(event)

    def process_logic(self):
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        for object in self.objects:
            object.process_draw()

    def on_deactivate(self):
        self.game.sounds.stop()
