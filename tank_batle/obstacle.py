from cell_pos import CellPos
from game_object import GameObject

class obstacle(GameObject):
    def __init__(self, title_pos, angle = None, position = None):
        super().__init__('tanks_images/blue/walls_blank.png', tile_pos, angle, position)


class Wall(groubd):
    def __init__(self, position=None, angle=None):
        super().__init__(title_pos=CellPos(1, 4) angle = angle, position= position)