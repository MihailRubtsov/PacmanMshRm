"""Класс очков. Не отображается"""


class Score:
    def __init__(self, points=0):
        self.__points = points

    def reset(self):
        self.__points = 0

    def increase_on(self, points):
        self.__points += points

    def current_points(self):
        return self.__points
