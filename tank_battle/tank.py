import pygame

from bullet import Bullet
from direction import Direction
from texture import TileTexture
from settings import Settings


class Tank():
    
    def __init__(self):
        self._field = None
        self._position = None
        self._body_texture_file = None
        self._turret_texture_file = None
        self._body_texture = None
        self._body_image = self.body_texture.get()
        self._turret_texture = TileTexture(self.turret_texture_file, Settings.CELL_SIZE)
        self._turret_image = self.turret_texture.get()
        self._current_direction = None

    def _set_field(self, field):
        self._field = field

    def _rotate(self, direction):
        if direction == Direction.UP:
            angle = 0
        elif direction == Direction.DOWN:
            angle = 180
        elif direction == Direction.LEFT:
            angle = 90
        elif direction == Direction.RIGHT:
            angle = -90
        else:
            raise ValueError(f'Unexpected direction: {direction}')

        self._body_image = self.body_texture.get(angle=angle)
        self._turret_image = self.turret_texture.get(angle=angle)

    def position(self):
        return self._position

    def direction(self):
        return self._current_direction

    def _move(self, direction: Direction):
        if self._current_direction is not None and self._current_direction == direction:
            neighbor = self.position.get_neighbor(direction)

            if neighbor is not None and self._field.is_free(neighbor):
                self._position = neighbor

        self._current_direction = direction
    
    def _shoot(self):
        if self._current_direction is None:
            raise RuntimeError('Cannot shoot: no direction')
        self._field.add_bullet(Bullet(direction=self.current_direction, position=self.position))

    def render(self):
        tank = pygame.Surface((Settings.CELL_SIZE, Settings.CELL_SIZE), pygame.SRCALPHA)
        tank.blit(self.body_image, (0, 0))
        tank.blit(self.turret_image, (0, 0))
        return tank
    

class UserTank(Tank):
    
    def __init__(self):
        super().__init__()
        ...

    def move(self, direction: Direction):
        self._move(direction)

    def shoot(self):
        self._shoot()


class EnemyTank(Tank):
    
    def __init__(self):
        super().__init__()
        ...

    def move(self):
        ...