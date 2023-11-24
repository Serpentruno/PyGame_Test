import pygame
import sys

from player import Player
from laser import Laser
from enemy import Enemy

#COSTINANTS
ANCHO = 800
ALTO = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,255,0)
BACKGROUND_COLOR = (100,60,180)

clock = pygame.time.Clock()

class Juego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Juego de Prueba")
        self.game_over = False
        self.color = BACKGROUND_COLOR
        self.speed_laser = 1
        self.speed_enemy = 1
        self.ancho_laser = 15
        self.alto_laser = 4
        self.color_laser = (255,0,0)
        self.player = Player(self)
        self.lasers = pygame.sprite.Group()
        self.total_lasers = 8
        self.enemies = pygame.sprite.Group()
        #pygame.mixer_music.load("MUSICA.wav")
        #pygame.mixer.music.play(-1) #ININITAMENTE
        #pygame.mixer.music.set_volume(0.2) #0 - 1
        self._create_enemy()

    def run_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.image = pygame.image.load("player_left.png")
                        self.player.direction = 0
                        self.player.move_left = True
                    if event.key == pygame.K_RIGHT:
                        self.player.image = pygame.image.load("player_right.png")
                        self.player.direction = 1
                        self.player.move_right = True
                    if event.key == pygame.K_UP:
                        self.player.move_up = True
                    if event.key == pygame.K_DOWN:
                        self.player.move_down = True

                    if event.key == pygame.K_SPACE:
                        self.fire_laser()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = False
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = False
                    if event.key == pygame.K_UP:
                        self.player.move_up = False
                    if event.key == pygame.K_DOWN:
                        self.player.move_down = False

            self.player.move()
            self.screen.fill(self.color)
            self.player.run()
            self.lasers.update()
            self.update_enemy()

            for laser in self.lasers.copy():
                if laser.direction == 0:
                    if laser.rect.right <= 0:
                        self.lasers.remove(laser)
                if laser.direction == 1:
                    if laser.rect.left >= ANCHO:
                        self.lasers.remove(laser)
                        

            for enemy in self.enemies.copy():
                if enemy.direction == 0:
                    if enemy.rect.right <= 0:
                        self.enemies.remove(enemy)
                        self._create_enemy()

                if enemy.direction == 1:
                    if enemy.rect.left >= ANCHO:
                        self.enemies.remove(enemy)
                        self._create_enemy()


            for laser in self.lasers.sprites():
                laser.draw_laser()

            self.enemies.draw(self.screen)
            pygame.display.flip()

    def fire_laser(self):
        if self.total_lasers != 0:
            new_laser = Laser(self)
            self.lasers.add(new_laser)
            self.total_lasers = self.total_lasers - 1

    def _create_enemy(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)
    
    def update_enemy(self):
        self.enemies.update()
        if not self.enemies:
            self._create_enemy()


if __name__ == "__main__":
    a = Juego()
    a.run_game()