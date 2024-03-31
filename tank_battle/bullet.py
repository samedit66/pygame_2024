from enum import Enum

import pygame

from direction import Direction
from texture import TileTexture
from settings import Settings


class Status(Enum):
    ALIVE = 0
    DESTROYED = 1


class Bullet():
    BULLET_MAX_DISTANCE = 5

    def __init__(self, direction, position):
        self.field = None
        self.position = position
        self.texture_file = './tanks_images/bullet.png'
        self.tile_size = 32
        self.texture = TileTexture(self.texture_file, self.tile_size)
        self.direction = direction
        self.status = Status.ALIVE
        self.distance = Bullet.BULLET_MAX_DISTANCE

    def set_field(self, field):
        self.field = field

    def move(self):
        if not self.field.can_move_to(self.position, self.direction):
            self.status = Status.DESTROYED
        else:
            self.position = self.position.get_neighbor(self.direction)

    def render(self):
        if self.status == Status.DESTROYED:
            raise RuntimeError('Cannot render a destroyed bullet')
        return self.texture.get()