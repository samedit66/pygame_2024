import pygame

from direction import Direction
from texture import TileTexture
from settings import Settings


class Tank():
    def __init__(self):
        self.field = None
        self.position = None
        self.body_texture_file = 'tanks_image/blue/body.png'
        self.turrent_texture_file = 'tanks_image/blue/turrent2.png'
        self.body_texture = TileTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self.body_texture.get()
        self.turrent_texture = TileTexture(self.turrent_texture_file, Settings.CELL_SIZE)
        self.turrent_image = self.turrent_texture.get()
        self.current_direction = None

    def set_field(self, field):
        self.field = field

    def set_position(self, position):
        self.position = position

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
        self.turrent_image = self.turrent_texture.get(angle=angle)

    def move(self, direction):
        if self.current_direction is not None and \
            self.current_direction == direction:

                if not self.field.can_move_to(self.position, direction):
                     return
                
                self.position = self.position.get_neighbour(direction)

        self.rotate(direction)
        self.current_direction = direction

    def render(self):
        tank = pygame.Surface((Settings.CELL_SIZE, Settings.CELL_SIZE), pygame.SRCALPHA)
        tank.blit(self.body_image, (0, 0))
        tank.blit(self.turrent_image, (0, 0))
        return tank