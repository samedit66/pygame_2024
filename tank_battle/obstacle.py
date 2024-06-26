from cell_pos import CellPos
from game_object import GameObject


class Obstacle(GameObject):

    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/red/towers_walls.png', tile_pos, angle, position)


class Wall(Obstacle):

    def __init__(self, position=None, angle=None):
        super().__init__(tile_pos=CellPos(1, 4), angle=angle, position=position)