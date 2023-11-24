import pygame

class Statistic:
    def __init__(self, a_game):
        self.restart()
        self.game = a_game

    def restart(self):
        self.remaining_lives = self.game.remaining_lives