from cellpos import CellPos 
from game_object import GameObject 

class Obstacle(GameObject):

    def __init__(self, tile_pos, angle = None, position = None):
        super().__init__("C:\\Users\\stude\\Documents\\game\\pygame_2024\\tank_battle\\tanks_images\\camo\\towers_walls.png", tile_pos, angle, position)

class WallCorner(Obstacle):

    def __init__(self, position = None, angle = None):
        super().__init__(tile_pos = CellPos(3,4), angle = angle, position = position)

class WallMiddle(Obstacle):

    def __init__(self, position = None, angle = None):
        super().__init__(tile_pos = CellPos(2,4), angle = angle, position = position)

class WallEnd(Obstacle):

    def __init__(self, position = None, angle = None):
        super().__init__(tile_pos = CellPos(1,4), angle = angle, position = position)

class Tower(Obstacle):

    def __init__(self, position = None, angle = None):
        super().__init__(tile_pos = CellPos(1,2), angle = angle, position = position)
