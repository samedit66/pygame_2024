from random import choice, random

import pygame

from bullet import Bullet
from direction import Direction
from texture import TileTexture
from settings import Settings
from traits import IsAlive

class Tank(IsAlive):

    def __init__(self):
        IsAlive.__init__(self)
        self.current_direction = None
        self.field = None
        self.position = None
        self.body_texture_file = 'tanks_images/desert/body.png'
        self.turret_texture_file = 'tanks_images/camo/turret2.png'
        self.body_texture = TileTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self.body_texture.get()
        self.turret_texture = TileTexture(self.turret_texture_file, Settings.CELL_SIZE)
        self.turret_image = self.turret_texture.get()

    def rotate(self, direction):
        if direction == Direction.UP:
            angle = 0
        elif direction == Direction.DOWN:
            angle = 180
        elif direction == Direction.LEFT:
            angle = 90
        elif direction == Direction.RIGHT:
            angle = -90

        self.body_image = self.body_texture.get(angle=angle)
        self.turret_image = self.turret_texture.get(angle=angle)

    def move(self, direction):
        if self.current_direction is not None and \
            self.current_direction == direction:

                if not self.field.can_move_to(self.position, direction):
                    return

                self.position = self.position.get_neighbor(direction)

        self.rotate(direction)
        self.current_direction = direction

    def render(self):
        tank = pygame.Surface((Settings.CELL_SIZE, Settings.CELL_SIZE), pygame.SRCALPHA)
        tank.blit(self.body_image, (0, 0))
        tank.blit(self.turret_image, (0, 0))
        return tank

    def set_field(self, field):
        self.field = field

    def set_position(self, position):
        self.position = position

    def shoot(self):
        neighbor = self.position.get_neighbor(self.current_direction)
        if neighbor is None:
            return False

        bullet = Bullet(self.current_direction)
        return self.field.put_at(bullet, neighbor)

class UserTank(Tank):
    pass

class EnemyTank(Tank):

    def move(self):
        if random() > 0.4:
            if self.current_direction is None:
                self.current_direction = choice(Direction.values())
            super().move(self.current_direction)
        else:
            possible_directions = [d for d in Direction.values()
                                    if d != self.current_direction]
            super().move(choice(possible_directions))

    def shoot(self):
        if random() > 0.5:
            super().shoot()