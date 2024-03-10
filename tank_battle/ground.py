from cell_pos import CellPoss
from game_object import GameObject


class Ground(GameObject):
    def __init__(self, texture_file, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/terrain.png', tile_pos, angle, position)

class Road(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPoss(3,4), angle = angle)

class Grass(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPoss(0,4), angle = angle)

class RoadCprner(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPoss(4,4), angle = angle)

class TripleRoad(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPoss(5, 4), angle = angle)

class Bush(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPoss(2,4), angle = angle)

