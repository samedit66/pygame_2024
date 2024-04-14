import pygame

from settings import Settings
from direction import Direction
from cell_pos import CellPos
from tank import UserTank, EnemyTank
from field import Field
from bullet import Bullet

class UserEvents:
    BULLET_FILES = pygame.USEREVENT + 1
    PLAYER_CAN_SHOOT = pygame.USEREVENT + 2
    ENEMY_TANK_CAN_MOVE = pygame.USEREVENT + 3
    ENEMY_CAN_SHOOT = pygame.USEREVENT + 4

class Game():

    def __init__(self):
        pygame.init()

        self.main_window = pygame.display.set_mode((Settings.PIXEL_WIDTH, Settings.PIXEL_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.field = Field()
        self.tank = UserTank()
        self.enemy = EnemyTank()
        self.field.put_at(self.tank, CellPos(0, 0))
        self.field.put_at(self.enemy, CellPos(0, 2))

        self.direction = None
        self.bullet_can_fly = False
        self.player_can_shoot = False
        self.enemy_can_move = False
        self.enemy_can_shoot = False
        pygame.time.set_timer(UserEvents.BULLET_FILES, 500)
        pygame.time.set_timer(UserEvents.PLAYER_CAN_SHOOT, 1200)
        pygame.time.set_timer(UserEvents.ENEMY_TANK_CAN_MOVE, 700)
        pygame.time.set_timer(UserEvents.ENEMY_CAN_SHOOT, 1000)

    def procces_input(self):
        self.direction = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

            elif event.type == UserEvents.BULLET_FILES:
                self.bullet_can_fly = True
            elif event.type == UserEvents.PLAYER_CAN_SHOOT:
                self.player_can_shoot = True
            elif event.type == UserEvents.ENEMY_CAN_SHOOT:
                self.enemy_can_shoot = True
            elif event.type == UserEvents.ENEMY_TANK_CAN_MOVE:
                self.enemy_can_move = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_a:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_s:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_w:
                    self.direction = Direction.UP
                elif event.key == pygame.K_SPACE:
                    if self.player_can_shoot:
                        self.tank.shoot()
                        self.player_can_shoot = False

    def update_game_state(self):
        if self.direction is not None:
            self.tank.move(self.direction)

        if self.bullet_can_fly:
            for bullet in self.field.get_bullets():
                bullet.move()
            self.field.clear_dead_units()
            self.bullet_can_fly = False

        if self.enemy_can_move:
            self.enemy.move()
            self.enemy_can_move = False

        if self.enemy_can_shoot:
            self.enemy.shoot()
            self.enemy_can_shoot = False

    def render(self):
        self.main_window.blit(self.field.render(), (0, 0))
        pygame.display.update()
        
    def game_loop(self):
        while self.running:
            self.procces_input()
            self.update_game_state()
            self.render()
            self.clock.tick(Settings.FPS)

        pygame.quit()

game = Game()
game.game_loop()