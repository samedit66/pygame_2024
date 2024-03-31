import pygame

from settings import Settings
from direction import Direction 
from cellpos import CellPos
from tank import Tank 
from field import Field 
from bullet import Bullet

class Game():

    def __init__(self):
        pygame.init()

        self.main_window = pygame.display.set_mode((Settings.PIXEL_WIDTH, Settings.PIXEL_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.field = Field()
        self.tank = Tank()
        self.bullet = Bullet(Direction.RIGHT)
        self.field.put_at(self.tank, CellPos(0,0))
        self.direction = None

    def process_input(self):
        self.direction = None 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT 
                elif event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP 

    def update_game_state(self):
        if self.direction is not None:
            self.tank.move(self.direction)

    def render(self):
        self.main_window.blit(self.field.render(), (0,0))
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