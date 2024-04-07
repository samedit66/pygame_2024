from cellpos import CellPos 
from game_object import GameObject




class Ground(GameObject):
    def __init__(self, tile_pos, angle = None, position = None):
        super().__init__("C:\\Users\\stude\\Documents\\game\\pygame_2024\\tank_battle\\tanks_images\\terrain.png", tile_pos, angle, position)


class Grass(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(0,3), angle = angle)


class Road(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(3,3), angle = angle)


class Bush(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(2,3), angle = angle)


class RoadCorner(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(4,3), angle = angle)


class TripleRoad(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(5,3), angle = angle)

class QuadRoad(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(6,3), angle = angle)

class Crater(Ground):
    def __init__(self, angle = None):
        super().__init__(tile_pos = CellPos(1,3), angle = angle)