from cell_pos import CellPos 
from game_object import GameObject


class Obstacle(GameObject):

    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/blue/towers_walls_blank.png', tile_pos, angle=angle, position=position)

class Wall(Obstacle):
    def __init__(self, angle=None, position=None):
        super().__init__(tile_pos=CellPos(1, 4), angle=angle, position=position)
