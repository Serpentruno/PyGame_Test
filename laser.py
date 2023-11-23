import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    def __init__(self, a_game) :
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.color_laser
        self.rect = pygame.Rect(0, 0, a_game.ancho_laser, a_game.alto_laser)
        self.rect.midtop = (a_game.player.rect.midtop[0] , a_game.player.rect.midtop[1] + 12)
        self.game = a_game
        self.direction = a_game.player.direction
        self.x = float(self.rect.x)
    
    def update(self):
        if self.direction == 0:
            self.x -= self.game.speed_laser
            self.rect.x = self.x
        elif self.direction == 1:
            self.x += self.game.speed_laser
            self.rect.x = self.x
            
    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)