import pygame

from settings import Settings
from direction import Direction
from cell_pos import CellPos
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
        self.field.put_at(self.bullet, CellPos(1,0))
        self.field.put_at(self.tank, CellPos(0,0))
        self.direction = None

        self.bullet_can_fly = True
        self.BULLET_FLIES = pygame.USEREVENT + 1
        pygame.time.set_timer(self.BULLET_FLIES, 500)

    def process_input(self):
        self.direction = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == self.BULLET_FLIES:
                if self.bullet.is_alive():
                    self.bullet.move()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_SPACE:
                    self.tank.shoot()

    def update_game_state(self):
        if not self.direction is None:
            self.tank.move(self.direction)
        if self.bullet_can_fly:
            for bullet in self.field.get_bullets():
                bullet.move()
        self.field.clear_dead_units()

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