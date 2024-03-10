from cell_pos import CellPoss
from game_object import GameObject


class Obstacle(GameObject):
    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_image/blue/towers_walls_blank.png', tile_pos, angle, position)

class Wall(Obstacle):
    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__(tile_pos= CellPoss(1,4), angle=angle, position= position)
        