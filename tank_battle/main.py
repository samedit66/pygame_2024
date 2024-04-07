from math import degrees, acos, sqrt

import pygame

from settings import Settings
from direction import Direction
from cell_pos import CellPos
from tank import Tank
from field import Field
    

class Game():

    def __init__(self):
        pygame.init()

        self.main_window = pygame.display.set_mode((Settings.PIXEL_WIDTH, Settings.PIXEL_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.field = Field()
        self.tank = Tank()
        self.field.put_at(self.tank, CellPos(0, 0))

        self.direction = None
    
    def process_input(self):
        self.direction = None
        self.shoot = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.direction = Direction.UP
                elif event.key == pygame.K_SPACE:
                    self.shoot = True

    def update_game_state(self):
        if self.direction is not None:
            self.tank.move(self.direction)
        if self.shoot:
            self.tank.shoot()
        for bullet in self.field.bullets:
            bullet.move()

    def render(self):
        self.main_window.blit(self.field.render(), (0, 0))
        pygame.display.update()

    def game_loop(self):
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(Settings.FPS)

        pygame.quit()


game = Game()
game.game_loop()