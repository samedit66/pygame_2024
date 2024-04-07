from cell_pos import CellPos
from game_object import GameObject


class Ground(GameObject):
<<<<<<< HEAD
    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/terrain.png', tile_pos, angle, position)

class Road(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPos(3,0), angle = angle)

class Grass(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPos(0,0), angle = angle)

class RoadCprner(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPos(4,0), angle = angle)

class TripleRoad(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPos(5, 0), angle = angle)

class Bush(Ground):
    def __init__(self, angle=None):
        super().__init__(tile_pos = CellPos(2,0), angle = angle)

=======

    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/terrain.png', tile_pos, angle, position)


class Grass(Ground):
    
    def __init__(self, angle=None):
        super().__init__(tile_pos=CellPos(0, 4), angle=angle)


class Road(Ground):
    
    def __init__(self, angle=None):
        super().__init__(tile_pos=CellPos(3, 4), angle=angle)


class RoadCorner(Ground):

    def __init__(self, angle=None):
        super().__init__(tile_pos=CellPos(4, 4), angle=angle)


class TripleRoad(Ground):

    def __init__(self, angle=None):
        super().__init__(tile_pos=CellPos(5, 4), angle=angle)


class Bush(Ground):

    def __init__(self, angle=None):
        super().__init__(tile_pos=CellPos(2, 4), angle=angle)
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
