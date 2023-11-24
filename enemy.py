import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen

        self.image = pygame.image.load("enemy_size.png")
        self.rect = self.image.get_rect()
        self.direction = random.choice([0,1])

        if self.direction == 0:
            self.rect.x = -self.rect.width
        else:
            self.rect.x = self.screen.get_rect().right
        self.rect.y = random.randint(0,self.screen.get_rect().bottom)

        self.x = float(self.rect.x)