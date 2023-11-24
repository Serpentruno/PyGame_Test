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
            self.image = pygame.image.load("enemy_left.png")
            self.rect.x = a_game.screen.get_rect().right
        else:
            self.image = pygame.image.load("enemy_right.png")
            self.rect.x = -self.rect.width 

        self.rect.y = random.randint(0,a_game.screen.get_rect().bottom - (2*self.rect.height))

        self.game = a_game
        self.x = float(self.rect.x)
    
    def update(self):
        if self.direction == 0:
            self.x -= self.game.speed_enemy
            self.rect.x = self.x
        elif self.direction == 1:
            self.x += self.game.speed_enemy
            self.rect.x = self.x
        
        self.player = self.game.player
        self.enemies = self.game.enemies
        
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.game.game_over = True