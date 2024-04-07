import pygame 

from direction import Direction
from texture import TileTexture
from settings import Settings
from traits import IsAlive


class Tank(IsAlive):
    def __init__(self):
        IsAlive.__init__(self)
        self.field = None
        self.current_direction = None
        self.position = None
        self.body_texture_file = "C:\\Users\\stude\\Documents\\game\\pygame_2024\\tank_battle\\tanks_images\\camo\\body.png"
        self.turret_texture_file = "C:\\Users\\stude\\Documents\\game\\pygame_2024\\tank_battle\\tanks_images\\camo\\turret1.png"
        self.body_texture = TileTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self.body_texture.get()
        self.turret_texture = TileTexture(self.turret_texture_file, Settings.CELL_SIZE)
        self.turret_image = self.turret_texture.get()

    def rotate(self, direction):
        if direction == Direction.UP:
            angle = 0
        elif direction == Direction.DOWN:
            angle = 180
        elif direction == Direction.RIGHT:
            angle = -90
        elif direction == Direction.LEFT:
            angle = 90
        
        self.body_image = self.body_texture.get(angle = angle)
        self.turret_image = self.turret_texture.get(angle = angle)

    def set_field(self, field):
        self.field = field 

    def set_position(self, position):
        self.position = position 

    def move(self, direction):
        if self.current_direction is not None and \
        self.current_direction == direction:
            if not self.field.can_move_to(self.position, direction):
                return
            self.position = self.position.get_neighbor(direction)
        self.rotate(direction)
        self.current_direction = direction

    def render(self):
        tank = pygame.Surface ((Settings.CELL_SIZE, Settings.CELL_SIZE), pygame.SRCALPHA)
        tank.blit(self.body_image, (0, 0))
        tank.blit(self.turret_image, (0, 0))
        return tank

    
    def shoot(self):
        neighbors = self.position.get_neighbor(self.current_direction)
        if neighbor is not None:
            return False 

        bullet = Bullet(neighbor)
        return self.field.put_at(bullet, neighbor)