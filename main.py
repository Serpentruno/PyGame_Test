import pygame
import random
import sys

from player import Player
from laser import Laser

#COSTINANTS
ANCHO = 800
ALTO = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,255,0)
BACKGROUND_COLOR = (100,60,180)

game_Over = False
clock = pygame.time.Clock()

class Juego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Juego de Prueba")
        self.color = BACKGROUND_COLOR
        self.speed_laser = 1
        self.ancho_laser = 15
        self.alto_laser = 4
        self.color_laser = (255,0,0)
        self.player = Player(self)
        self.lasers = pygame.sprite.Group()

    def run_game(self):
        while not game_Over:
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
            for laser in self.lasers.sprites():
                laser.draw_laser()
            pygame.display.flip()

    def fire_laser(self):
        new_laser = Laser(self)
        self.lasers.add(new_laser)
if __name__ == "__main__":
    a = Juego()
    a.run_game()

""" pygame.init()


#PLAYER
player_Size = 50
player_Pos = [ANCHO/2, ALTO - player_Size * 2]

#ENEMY
enemy_Size = 50
enemy_Pos = [random.randrange(0, ANCHO - enemy_Size, enemy_Size), 0]

#WINDOW
window = pygame.display.set_mode((ANCHO,ALTO))


def detect_Crash(player_Pos, enemy_Pos):
    px = player_Pos[0]
    py = player_Pos[1]
    ex = enemy_Pos[0]
    ey = enemy_Pos[1]

    if (ex >= px and ex < (px + player_Size)) or (px >= ex and px < (ex + enemy_Size)):
        if (ey >= py and ey < (py + player_Size)) or (py >= ey and py < (ey + enemy_Size)):
            return True
        
while not game_Over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_Pos[0]
            y = player_Pos[1]
            if event.key == pygame.K_UP:
                y -= player_Size
            if event.key == pygame.K_DOWN:
                y += player_Size
            if event.key == pygame.K_LEFT:
                x -= player_Size
            if event.key == pygame.K_RIGHT:
                x += player_Size

            player_Pos[0] = x
            player_Pos[1] = y

    window.fill(BACKGROUND_COLOR)

    if enemy_Pos[1] >= 0 and enemy_Pos[1] < ANCHO:
        enemy_Pos[1] += 1
    else:
        enemy_Pos[0] = random.randrange(0,ANCHO - enemy_Size, enemy_Size)
        enemy_Pos[1] = 0
    
    #CRUSH
    if detect_Crash(player_Pos, enemy_Pos):
        game_Over = True

    #DRAW ENEMY
    pygame.draw.rect(window, BLUE, 
                     (enemy_Pos[0], enemy_Pos[1],
                      enemy_Size, enemy_Size))

    #DRAW PLAYER
    pygame.draw.rect(window,RED, 
                     (player_Pos[0],player_Pos[1], 
                      player_Size, player_Size))
    
    clock.tick(100)
    pygame.display.update() 
    
    AGREGANDO PARA PROBAR PUSH
    Haciendo la Utlima PRUEBA 
    
    .... """