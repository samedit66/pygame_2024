from cell_pos import CellPos
from game_object import GameObject


class Obstacle(GameObject):
<<<<<<< HEAD
    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/blue/towers_walls_blank.png', tile_pos, angle, position)

class Wall(Obstacle):
    def __init__(self, angle=None, position=None):
        super().__init__(tile_pos= CellPos(2,4), angle=angle, position= position)
        
=======

    def __init__(self, tile_pos, angle=None, position=None):
        super().__init__('tanks_images/red/towers_walls.png', tile_pos, angle, position)


class Wall(Obstacle):

    def __init__(self, position=None, angle=None):
        super().__init__(tile_pos=CellPos(1, 4), angle=angle, position=position)
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
