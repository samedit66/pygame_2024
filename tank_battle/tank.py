import pygame

<<<<<<< HEAD
=======
from bullet import Bullet
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
from direction import Direction
from texture import TileTexture
from settings import Settings


class Tank():
<<<<<<< HEAD
    def __init__(self):
        self.field = None
        self.position = None
        self.body_texture_file = 'tanks_images/blue/body.png'
        self.turrent_texture_file = 'tanks_images/blue/turret2.png'
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
=======
    
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
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
        if direction == Direction.UP:
            angle = 0
        elif direction == Direction.DOWN:
            angle = 180
        elif direction == Direction.LEFT:
            angle = 90
        elif direction == Direction.RIGHT:
            angle = -90
<<<<<<< HEAD
        
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
=======
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
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495

    def render(self):
        tank = pygame.Surface((Settings.CELL_SIZE, Settings.CELL_SIZE), pygame.SRCALPHA)
        tank.blit(self.body_image, (0, 0))
<<<<<<< HEAD
        tank.blit(self.turrent_image, (0, 0))
        return tank
=======
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
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
