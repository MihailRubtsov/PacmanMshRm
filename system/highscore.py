"""Класс, работающий с рекордами. Не отображается"""
from constants import SAVE_PATH


class Highscore:
    SAVE_FILE = SAVE_PATH
    HIGHSCORE_COUNT = 10

    def __init__(self):
        self.highscores = []
        self.load_from_file()

    def load_from_file(self):
        with open(self.SAVE_FILE, 'r') as save_file:
            self.highscores = []
            count = int(save_file.readline())
            for i in range(count):
                result = save_file.readline().split()
                self.highscores.append([result[0], int(result[1])])

    def save_to_file(self):
        with open(self.SAVE_FILE, 'w') as save_file:
            save_file.write(f'{len(self.highscores)}\n')
            for i in range(len(self.highscores)):
                save_file.write(f'{self.highscores[i][0]} {self.highscores[i][1]}\n')

    def clean_all_results(self):
        with open(self.SAVE_FILE, 'w') as save_file:
            save_file.write('0\n')
            self.highscores = []

    def add_new_result(self, name, new_result):
        insert_position = self.is_highscore(new_result)
        self.highscores = self.highscores[:insert_position] + [[name, new_result]] + self.highscores[insert_position:]
        if len(self.highscores) > self.HIGHSCORE_COUNT:
            self.highscores = self.highscores[:self.HIGHSCORE_COUNT]

    def is_highscore(self, new_result):
        insert_position = 0
        while insert_position < len(self.highscores) and self.highscores[insert_position][1] > new_result:
            insert_position += 1
        return insert_position
