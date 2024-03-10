import Pygame 

from direction import Direction
from texture import TileTexture
from settings import Settings



class Tank():
    def __init__(self):
        self.field = None
        self.current_direction = None
        self.position = None
        self.body_texture_file = 'tanks_images/green/body.png'
        self.turret_texture_file = 'tanks_images/purple/turret1.png'
        self.body_texture = TileTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self.body_texture.get()
        self.turret_texture = TileTexture(self.turret_texture_file, Settings.CELL_SIZE)
        self.turret_image = self.turret_texture.get()

    def rotate(self, direction):
        if direction == Direction.UP:
            angle = 0
        elif direction = Direction.DOWN:
            angle = 180
        elif direction = Direction.RIGHT:
            angle = -90
        elif direction = Direction.LEFT:
            angle = 90
        
        self.body_image = self.body_texture_get(angle = angle)
        self.turet_image = self.turret_texture_get(angle = angle)

    def set_field(self, field)
        self.field = field 

    def set_position(self, position):
        self.position = position 

    def move(self, direction):
        if self.current_direction is not None and \
        self.current_direction == direction:
            if not self.field.can_moce_to(self.position, direction):
                return
            self.position = self.position.get_neighbor(direction)
        self.rotate(direction)
        self.current_direction = direction

    def render(self):
        tank = pygame.Surface ((Settings.CELL_SIZE, Settings.CELL_SZIE), pygame.SRCALPHA)
        tank.blit(self.body.image, (0, 0))
        tank.blit(self.turret_image, (0, 0))
        return tank